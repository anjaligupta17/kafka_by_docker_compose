from confluent_kafka import Consumer, KafkaError

# Kafka configuration
kafka_bootstrap_servers = 'kafka:9092'  # Use service name 'kafka' instead of localhost
kafka_topic = 'test_topic'

# Kafka Consumer configuration
consumer_conf = {
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': 'my_unique_consumer_group_id',
    'auto.offset.reset': 'earliest'
}

# Create Kafka Consumer
consumer = Consumer(consumer_conf)
consumer.subscribe([kafka_topic])

# File to store consumed messages
output_file = 'consumed_messages.txt'

# Main loop to consume messages
try:
    with open(output_file, 'a') as f:
        while True:
            msg = consumer.poll(10.0)
            if msg is None:
                continue
            if msg.error():
                error_code = msg.error().code()
                # Handle specific error codes here (e.g., handle PARTITION_EOF differently)
                if error_code == KafkaError._PARTITION_EOF:
                    continue
                else:
                    # Log the error for further investigation
                    print(f"Error consuming message: {msg.error()}")
                    # Consider retrying or taking other actions based on the error
            consumed_message = msg.value().decode("utf-8")
            f.write(consumed_message + '\n')
            print(f'Received message: {consumed_message}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

print(f"Consumed messages are saved to {output_file}")
