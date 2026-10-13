# GitHub → Colab execution

This repository is intended to be the source of truth for the Capstone B project.

## Prerequisites

- Python 3.12+ and `uv` on a local Linux/macOS machine
- Google account with Colab access
- Google Colab CLI installed and authenticated
- The official dataset available under the path/schema expected by the notebooks
- Valid credentials and configuration if the notebooks use a hosted LLM/ADK backend

Install CLI:

```bash
uv tool install google-colab-cli
```

Authenticate using the current instructions in the [official CLI repository](https://github.com/googlecolab/google-colab-cli). Do not commit credentials.

## Run

From the repository root, create a session (optionally choose an accelerator supported by your account):

```bash
colab new -s sahayak
```

Run the notebooks in dependency order:

```bash
colab exec -s sahayak -f adk_foundations.ipynb
colab exec -s sahayak -f data_understanding_and_baseline.ipynb
colab exec -s sahayak -f agent_pipeline_development.ipynb
colab exec -s sahayak -f agent_evaluation_and_optimisation.ipynb
```

Or use `bash scripts/run_colab_submission.sh` after checking the command syntax against the installed CLI version.

Export execution history:

```bash
mkdir -p execution_logs
colab log -s sahayak -o execution_logs/sahayak_execution_log.md
```

## Finalization gates

1. Confirm the full official 853/212 split is loaded; no synthetic/offline fallback is silently used.
2. Execute every code cell and inspect errors and visible outputs.
3. Confirm all demonstration traces call the actual pipeline.
4. Calculate final acceptance metrics directly from the held-out DataFrame.
5. Do not tune on the held-out split.
6. Regenerate `final_report.pdf` from those outputs and reconcile all reported metrics.
7. Commit executed notebooks, final report, and permitted execution evidence.

A successful notebook execution is not proof of clinical safety. Report failed safety targets explicitly.
