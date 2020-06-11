import pika
import json

from logger import logger


def send_to_backend(type, queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost',
        5672,
        'ducxwill',
        pika.PlainCredentials('ducxwill', 'ducxwill'),
    ))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True, auto_delete=False,
                          exclusive=False)
    channel.basic_publish(
        exchange=queue,
        routing_key=queue,
        body=json.dumps(message),
        properties=pika.BasicProperties(type=type),
    )
    connection.close()

    logger.info('message sent to backend: {}'.format(message))


def send_to_monitor():
    pass
