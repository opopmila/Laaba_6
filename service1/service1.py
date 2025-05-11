import asyncio
import aio_pika
import logging
from prometheus_client import start_http_server, Counter

# Метрики
MESSAGES_PROCESSED = Counter("service1_messages_processed", "Total messages processed by Service 1")

async def main():
    connection = await aio_pika.connect_robust("amqp://admin:admin@rabbitmq:5672")
    channel = await connection.channel()
    queue = await channel.declare_queue("service1_queue")
    async for message in queue.iterator():
        async with message.process():
            MESSAGES_PROCESSED.inc()
            print(f"Service 1 processed: {message.body.decode()}")

if __name__ == "__main__":
    start_http_server(8001)
    asyncio.run(main())
