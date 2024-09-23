# Dockerfile for FastAPI API
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./code/deployment/api/model_api.py /app/model_api.py
COPY ./models/trained_model.pkl /app/models/

RUN pip install pydantic scikit-learn

CMD ["uvicorn", "model_api:app", "--host", "0.0.0.0", "--port", "8000"]

