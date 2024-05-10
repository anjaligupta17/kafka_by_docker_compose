FROM python:3.9

# Install Kafka client library
RUN pip install confluent-kafka

# Set the working directory inside the container
WORKDIR /app

# Copy the consumer application code into the container
COPY consumer.py .

# Command to run the consumer application when the container starts
CMD ["python", "consumer.py"]
