
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("KafkaIntegration") \
    .getOrCreate()

# Read data from Kafka topic into DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "your_topic_name") \
    .load()

# Perform transformations on DataFrame
# For example:
# transformed_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Start streaming query
query = transformed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
