#!/usr/bin/env bash
set -euo pipefail

SESSION="${COLAB_SESSION:-sahayak}"
GPU_ARGS=()
if [[ "${SAHAYAK_COLAB_GPU:-}" != "" ]]; then
  GPU_ARGS=(--gpu "${SAHAYAK_COLAB_GPU}")
fi

command -v colab >/dev/null 2>&1 || {
  echo "Missing Google Colab CLI. Install with: uv tool install google-colab-cli" >&2
  exit 2
}

if [[ ! -f adk_foundations.ipynb || ! -f data_understanding_and_baseline.ipynb || ! -f agent_pipeline_development.ipynb || ! -f agent_evaluation_and_optimisation.ipynb ]]; then
  echo "Run from repository root; one or more canonical notebooks are missing." >&2
  exit 2
fi

# Provision a session only if one does not already exist; command behavior depends
# on the installed CLI version, so create the session explicitly before running.
colab new -s "${SESSION}" "${GPU_ARGS[@]}"

for notebook in   adk_foundations.ipynb   data_understanding_and_baseline.ipynb   agent_pipeline_development.ipynb   agent_evaluation_and_optimisation.ipynb
do
  echo "Executing ${notebook}"
  colab exec -s "${SESSION}" -f "${notebook}"
done

mkdir -p execution_logs
colab log -s "${SESSION}" -o execution_logs/sahayak_execution_log.md
echo "Execution finished. Review the returned executed notebooks and log before updating final_report.pdf."
