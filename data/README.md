# Dataset setup

This directory is reserved for the Capstone B dataset files required by the notebooks.

## Before running

1. Inspect the original UpGrad Capstone B Starter Package and Capstone B Starter Files archives supplied with the project.
2. Place the official train and test dataset files here, preserving the filenames and schema expected by `data_loader.py` / the notebooks.
3. Do not fabricate, resample, or silently substitute data if the official files are unavailable.
4. Confirm the expected split counts from the official dataset: 853 training cases and 212 held-out test cases.
5. Keep the held-out test split untouched until final evaluation. Do not tune policy thresholds against it.

## Data handling

Do not commit private, licensed, or otherwise restricted data unless the course explicitly permits it. If the official dataset cannot be redistributed, document the official source and exact retrieval steps here and keep the data out of Git. The notebooks must fail clearly rather than report old aggregate metrics as a new evaluation.
