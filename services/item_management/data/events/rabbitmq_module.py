import pika

class RabbitMQ:
    def __init__(self):
        self.connection = None

    async def connection(self):
        # Establish a connection with RabbitMQ server.
        self.connection = await pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq:15672'))
        return self

    async def getChannel(self):
        return self.connection.channel()

    async def close(self):
        # Close a connection with RabbitMQ server.
        await self.connection.close()
        return self

    async def publish(self, queue, exchange, body):
        channel = self.getChannel
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange=exchange, routing_key=queue, body=body)
        return self

