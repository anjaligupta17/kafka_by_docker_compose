# Use the official Python base image
FROM python:3.9

# Install Kafka client library and requests module
RUN pip install kafka-python requests

# Set the working directory inside the container
WORKDIR /app

# Copy the producer application code into the container
COPY producer.py /app/

# Command to run the producer application when the container starts
CMD ["python", "producer.py"]
