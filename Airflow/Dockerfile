# Use the official Airflow image from Docker Hub
FROM apache/airflow:latest

# Set the working directory inside the container
WORKDIR /usr/local/airflow

# Install any additional Python packages if needed
# For example:
# RUN pip install <package-name>

# Copy the DAGs, logs, and plugins directories from the host into the container
COPY ./dags /usr/local/airflow/dags
COPY ./logs /usr/local/airflow/logs
COPY ./plugins /usr/local/airflow/plugins

# Expose the Airflow webserver port
EXPOSE 8080

# Start the Airflow webserver when the container starts
CMD ["webserver"]
