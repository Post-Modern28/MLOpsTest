# Dockerfile for Streamlit app
FROM python:3.9

WORKDIR /app

COPY ./web_app.py /app/

RUN pip install streamlit requests

CMD ["streamlit", "run", "web_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
