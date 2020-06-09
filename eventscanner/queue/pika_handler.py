import pika
import json


def send_in_queue(type, queue, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost',
        5672,
        'mywill',
        pika.PlainCredentials('java', 'java'),
    ))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True, auto_delete=False,
                          exclusive=False)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=json.dumps({'status': 'COMMITTED'}),
        properties=pika.BasicProperties(type=type),
    )
    connection.close()
