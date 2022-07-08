from core.modules.kafka_trinhdq.producer_service import ProducerService
from core.modules.kafka_trinhdq.consume_service import ConsumeService

if __name__ == "__main__":
    producer_service = ProducerService()
    producer_service.send(topic='order-events', key='1', value='123')
    producer_service.send(topic='order-events', key='2', value='trinh')
    producer_service.send(topic='order-events', key='1', value='trinh1')

    consume_service = ConsumeService()
    result = consume_service.subscribe('order-events')

    print(f'Data: {result}')


