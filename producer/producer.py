from kafka import KafkaProducer
import requests
import json

# Kafka configuration
kafka_topic = 'work'  # Define Kafka topic
kafka_brokers = ['localhost:9092']  # Define Kafka brokers

# Function to fetch data from the API
def fetch_data():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    return json.dumps(data)

# Create Kafka producer
kafka_producer = KafkaProducer(bootstrap_servers=kafka_brokers,
                               api_version=(0, 11, 5))

# Main function to produce data to Kafka topic
def produce_to_kafka():
    while True:
        try:
            data = fetch_data()
            kafka_producer.send(kafka_topic, data.encode('utf-8'))
            kafka_producer.flush()
            print("Data sent successfully")
        except Exception as e:
            print(f"Error: {e}")
            # Handle the error here as needed

# Run the producer
if __name__ == '__main__':
    produce_to_kafka()
