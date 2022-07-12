import json

from confluent_kafka import Consumer

consumer = Consumer({
    'bootstrap.servers': 'broker',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['test'])
total_count = 0
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            # No message available within timeout.
            # Initial message consumption may take up to
            # `session.timeout.ms` for the consumer group to
            # rebalance and start consuming
            print("Waiting for message or event/error in poll()")
            continue
        elif msg.error():
            print('error: {}'.format(msg.error()))
        else:
            # Check for Kafka message
            record_key = msg.key()
            record_value = msg.value()
            data = json.loads(record_value)
            count = data['count']
            total_count += count
            print("Consumed record with key {} and value {}, \
                     and updated total count to {}"
                  .format(record_key, record_value, total_count))
except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
