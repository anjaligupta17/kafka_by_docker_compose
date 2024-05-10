
from confluent_kafka import Consumer, KafkaError

# Kafka configuration
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'work'

# Kafka Consumer configuration
consumer_conf = {
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': 'my_unique_consumer_group_id',
    'auto.offset.reset': 'earliest'
}

# Create Kafka Consumer
consumer = Consumer(consumer_conf)
consumer.subscribe([kafka_topic])

# Main loop to consume messages
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print(f'Received message: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
