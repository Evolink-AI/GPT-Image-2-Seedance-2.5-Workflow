#!/usr/bin/env bash
# Source this file from Bash. Creation is intentionally separate from polling.
set -euo pipefail

submit_task() {
  local kind=$1 payload=$2 receipt=$3
  case "$kind" in images|videos) ;; *) echo 'Expected images or videos' >&2; return 2 ;; esac
  : "${EVOLINK_API_KEY:?Set EVOLINK_API_KEY in your environment}"
  jq -e 'type == "object" and (.model | type == "string")' "$payload" >/dev/null
  # Atomic reservation: rerunning must never silently create a second paid task.
  if ! mkdir "$receipt"; then
    echo "Receipt exists: $receipt. Inspect its response and resume the original task." >&2
    return 2
  fi
  cp "$payload" "$receipt/request.json"
  if ! curl --silent --show-error --fail-with-body --max-time 120 \
    --request POST "https://api.evolink.ai/v1/$kind/generations" \
    --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
    --header 'Content-Type: application/json' \
    --data-binary "@$payload" --output "$receipt/created.json"; then
    echo "Submission did not return success. Inspect $receipt/created.json; do not automatically repeat POST." >&2
    return 1
  fi
  jq -er '.id | select(type == "string" and length > 0)' "$receipt/created.json" > "$receipt/task-id.txt"
  echo "Task saved in $receipt/task-id.txt"
}

wait_task() {
  local task_id=$1 result_file=$2 timeout=${3:-900}
  local deadline status
  : "${EVOLINK_API_KEY:?Set EVOLINK_API_KEY in your environment}"
  [[ "$task_id" =~ ^[A-Za-z0-9_-]+$ ]] || { echo 'Invalid task ID' >&2; return 2; }
  [[ "$timeout" =~ ^[1-9][0-9]*$ ]] || { echo 'Timeout must be positive seconds' >&2; return 2; }
  deadline=$((SECONDS + timeout))
  while (( SECONDS < deadline )); do
    # A failed GET stops waiting, never submits a new task. Run wait_task again.
    curl --silent --show-error --fail-with-body --max-time 60 \
      "https://api.evolink.ai/v1/tasks/$task_id" \
      --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
      --output "$result_file" || return 1
    status=$(jq -er '.status' "$result_file") || return 1
    case "$status" in
      completed) jq -e '.results | type == "array" and length > 0' "$result_file" >/dev/null; return ;;
      failed) jq '.error' "$result_file" >&2; return 1 ;;
      pending|processing) sleep 5 ;;
      *) echo "Unexpected status: $status. Inspect $result_file" >&2; return 1 ;;
    esac
  done
  echo "Stopped waiting for $task_id; the submitted task may still be running. Resume with the same ID." >&2
  return 1
}

download_result() {
  local result_file=$1 output_file=$2 url
  url=$(jq -er 'select(.status == "completed") | .results[0] | select(type == "string")' "$result_file") || return 1
  # Result download gets no API authorization header.
  curl --fail --location --proto '=https' --proto-redir '=https' \
    --output "$output_file" "$url"
}
