# Insurance AI API

A simple MVP backend for insurance risk prediction built with FastAPI and scikit-learn.

## Features

- `/health` health check
- `/predict` risk prediction endpoint
- `/model/info` model metadata endpoint

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker
```bash
docker build -t insurance-ai-api .
docker run -p 8000:8000 insurance-ai-api
```

## Example prediction request
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "bmi": 31.2,
    "smoker": true,
    "region": "southwest",
    "children": 2
  }'
```

## Run tests
```bash
pytest tests/
```