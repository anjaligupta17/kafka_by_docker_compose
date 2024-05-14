# Use a base image that includes Java and Python
FROM openjdk:8-jre-slim

# Install Python and necessary libraries
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PYTHONPATH=${SPARK_HOME}/python:$PYTHONPATH
ENV PATH=${SPARK_HOME}/bin:$PATH

# Download and install Spark
RUN curl -O https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz && \
    tar xf spark-3.2.0-bin-hadoop3.2.tgz && \
    mv spark-3.2.0-bin-hadoop3.2 ${SPARK_HOME} && \
    rm spark-3.2.0-bin-hadoop3.2.tgz

# Set the working directory
WORKDIR /app

# Copy your PySpark application code into the container
COPY . /app

# Expose port for Spark UI
EXPOSE 4040

# Install Kafka dependencies
RUN pip3 install kafka-python

# Run your PySpark application
CMD ["spark-submit", "--master", "local[*]", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0", "your_script.py"]
