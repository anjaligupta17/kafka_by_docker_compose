from confluent_kafka import Producer
import csv

# Kafka configuration
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'your_topic_name'

# Function to read data from CSV file
def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

# Kafka Producer callback function
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Create Kafka Producer
producer = Producer({'bootstrap.servers': kafka_bootstrap_servers})

# Main function to produce messages to Kafka topic
def produce_to_kafka(file_path):
    for row in read_csv(file_path):
        # Produce data to Kafka topic
        producer.produce(kafka_topic, str(row).encode('utf-8'), callback=delivery_report)
        # Wait for message to be delivered
        producer.poll(0.5)

# Run the producer
if __name__ == '__main__':
    csv_file_path = 'your_csv_file.csv'
    produce_to_kafka(csv_file_path)
