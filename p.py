from confluent_kafka import Producer, KafkaError
import json


if __name__ == '__main__':


    # Create Producer instance
    producer = Producer({
        'bootstrap.servers': 'localhost:9092',
        'security.protocol': 'PLAINTEXT',
    })

    # Create topic if needed


    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):

        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))

    for n in range(10):
        record_key = "alice"
        record_value = json.dumps({'count': n})
        # print("Producing record: {}\t{}".format(record_key, record_value))
        producer.produce('test', key=record_key, value=record_value, on_delivery=acked)
        # p.poll() serves delivery reports (on_delivery)
        # from previous produce() calls.
        producer.poll(1.0)

    producer.flush()

    # print("{} messages were produced to topic {}!".format(delivered_records, topic))