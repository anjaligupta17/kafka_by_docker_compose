
from kafka import KafkaProducer
import requests
import json

# Kafka configuration
bootstrap_servers = 'PLAINTEXT://localhost:9092'
topic = 'work'

# Function to fetch data from the API
def fetch_data():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    return json.dumps(data)

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
              api_version=(0,11,5),
              value_serializer=lambda x: dumps(x).encode('utf-8'))

# Main function to produce data to Kafka topic
def produce_to_kafka():
    while True:
        data = fetch_data()
        producer.send(topic, data.encode('utf-8'))

# Run the producer
if __name__ == '__main__':
    produce_to_kafka()
