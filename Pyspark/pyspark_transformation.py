from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Create a SparkSession
spark = SparkSession.builder \
    .appName("KafkaSparkIntegration") \
    .getOrCreate()

# Define the Kafka topic to subscribe to
kafka_topic = "your_topic_name"

# Define the schema for the incoming Kafka messages
schema = StructType().add("key", StringType()).add("value", StringType())

# Read data from Kafka
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", kafka_topic) \
    .load()

# Convert Kafka message value from binary to string
value_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Define schema for JSON data
json_schema = StructType().add("field1", StringType()).add("field2", StringType())

# Parse JSON data
parsed_df = value_df.select(from_json(col("value"), json_schema).alias("data")).select("data.*")

# Perform further processing as needed
parsed_df.printSchema()

# Start the streaming query
query = parsed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the streaming query to finish
query.awaitTermination()
