FROM python:3.9
WORKDIR /app
COPY gateway.py .
RUN pip install fastapi uvicorn aio-pika opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp prometheus-client
CMD ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "8000"]
