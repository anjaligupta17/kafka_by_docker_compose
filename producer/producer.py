
from kafka import KafkaProducer
import requests
import json

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'your_topic'

# Function to fetch data from the API
def fetch_data():
    response = requests.get('your_api_endpoint')
    data = response.json()
    return json.dumps(data)

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Main function to produce data to Kafka topic
def produce_to_kafka():
    while True:
        data = fetch_data()
        producer.send(topic, data.encode('utf-8'))

# Run the producer
if __name__ == '__main__':
    produce_to_kafka()
