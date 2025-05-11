FROM python:3.9
WORKDIR /app
COPY service1.py .
RUN pip install aio-pika opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp prometheus-client
CMD ["python", "service1.py"]
