import requests
from kafka import KafkaProducer
import time

def main():
    # Kafka broker address
    bootstrap_servers = 'kafka:9092'
    # Kafka topic name
    topic = 'test_topic'

    # Create KafkaProducer instance
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Buffer to store data before writing to file
    data_buffer = []

    try:
        while True:
            # Retrieve data from API
            data = fetch_api_data()
            
            # Send data to Kafka topic
            producer.send(topic, value=data.encode())
            print(f"Produced to Kafka: {data}")

            # Append data to buffer
            data_buffer.append(data)

            # Flush buffer to file every 10 records
            if len(data_buffer) >= 10:
                flush_data_to_file(data_buffer)
                data_buffer = []  # Clear the buffer

            time.sleep(1)  # Adjust the delay as needed
    except KeyboardInterrupt:
        print("Stopping producer...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Flush any remaining data in the buffer to file before closing
        if data_buffer:
            flush_data_to_file(data_buffer)
        producer.close()

def fetch_api_data():
    # Replace 'https://example.com/api' with your API endpoint
    response = requests.get('https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=288&aggregate=5')
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

def flush_data_to_file(data_buffer):
    # Write data from buffer to file
    with open('data.txt', 'a') as file:
        for data in data_buffer:
            file.write(data + '\n')

if __name__ == "__main__":
    main()
