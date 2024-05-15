# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
        curl \
        default-libmysqlclient-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        libpq-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Apache Airflow with extras
RUN pip install 'apache-airflow[celery,crypto,jdbc,mysql,postgres,ssh,statsd]==2.2.0'

# Initialize Airflow database
RUN airflow db init

# Create a directory for logs and dags
RUN mkdir -p /opt/airflow/logs && mkdir -p /opt/airflow/dags

# Expose the port for Airflow webserver
EXPOSE 8080

# Start Airflow webserver
CMD ["airflow", "webserver", "--port", "8080"]
