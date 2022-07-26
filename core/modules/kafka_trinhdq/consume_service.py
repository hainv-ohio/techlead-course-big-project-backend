import json
from confluent_kafka import Consumer
    
class ConsumeService:
    running = True
    def __init__(self) -> None:
        pass

    def create(self, group_id):
        conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': group_id,
        'auto.offset.reset': 'smallest'}
        # conf = {
        #         'bootstrap.servers': 'localhost:9092',
        #         'auto.offset.reset': 'largest',
        #         'enable.auto.commit': 'false',
        #         'max.poll.interval.ms': '86400000'
        # }
        
        return Consumer(conf)

    def subscribe(self, topics):
        try:
            consumer = self.create(1)
            consumer.subscribe([topics])
            data = []
            while True:
                msg = consumer.poll(0)
                if msg is None:
                    # No message available within timeout.
                    # Initial message consumption may take up to
                    # `session.timeout.ms` for the consumer group to
                    # rebalance and start consuming
                    # print("Waiting for message or event/error in poll()")
                    continue
                elif msg.error():
                    print('error: {}'.format(msg.error()))
                else:
                    # Check for Kafka message
                    record_key = msg.key()
                    record_value = msg.value()
                    # data[record_key] = json.loads(record_value)
                    data.append(msg)
                    print(f'Data: {data}')
                    # return

                    # count = count(data)
                    # total_count += count
                    # print("Consumed record with key {} and value {}, \
                    #     and updated total count to {}"
                        # .format(record_key, record_value, total_count))   
        except KeyboardInterrupt:
            pass
        finally:
            # Leave group and commit final offsets
            consumer.close()



            