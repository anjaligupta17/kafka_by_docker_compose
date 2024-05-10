from confluent_kafka import Consumer, KafkaError

# Kafka configuration
kafka_bootstrap_servers = 'kafka:9092'  # Use service name 'kafka' instead of localhost
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

# List to store consumed messages
consumed_messages = []

# Main loop to consume messages
try:
    while True:
        msg = consumer.poll(1.0)
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
        consumed_messages.append(msg.value().decode("utf-8"))
        print(f'Received message: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

# Print the consumed messages
print("Consumed messages:")
for message in consumed_messages:
    print(message)
