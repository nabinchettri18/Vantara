# Vantara — Customer Behavior Prediction Platform

End-to-end machine learning and deep learning platform for customer churn, lifetime value, purchase behavior, segmentation, anomaly detection, explainability, API serving, and dashboarding.

Built according to the Vantara Retail Solutions Product Requirements Document (v1.0).

## Project Status

**Day 1 — Data Foundation**

Current work:
- Repository scaffolding
- Python dependency specification
- UCI Online Retail II download pipeline
- Non-destructive dataset validation
- FastAPI and Streamlit application skeletons

## Day 1 — Local Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Download the dataset:

```powershell
python src\data\download_dataset.py
```

Run validation:

```powershell
python src\data\validate_dataset.py
```

The raw dataset is intentionally excluded from Git via `.gitignore`.

## Architecture

```
Raw Transactions
      ↓
Data Validation & Cleaning
      ↓
Customer Feature Engineering
      ↓
ML / Deep Learning Models
      ↓
Segmentation + Explainability
      ↓
FastAPI + PostgreSQL
      ↓
Streamlit Dashboard
```

## Branching

Current development branch:

`day-1-data-foundation`

The `main` branch is kept stable while the project is built incrementally.
