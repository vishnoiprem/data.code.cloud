# Q12: Exactly-once Kafka to Redshift using Spark Structured Streaming (Simulated for local)

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col
import datetime

# Init Spark session
spark = SparkSession.builder \
    .appName("Q12_Kafka_Redshift_ExactlyOnce") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Simulated Kafka stream from file source
kafka_stream = spark.readStream \
    .schema("trade_id STRING, amount DOUBLE, timestamp STRING") \
    .option("maxFilesPerTrigger", 1) \
    .csv("data/kafka_stream_simulated/")  # Replace with actual Kafka config in real case

# Transform and enrich
df_transformed = kafka_stream.withColumn("ingestion_ts", expr("current_timestamp()"))

# Simulate Redshift upsert logic via write to Delta staging
staging_path = "output/redshift_staging/"
checkpoint_path = "output/redshift_checkpoints/"

# Write as Delta table (simulate idempotent UPSERT into Redshift)
query = df_transformed.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpoint_path) \
    .option("path", staging_path) \
    .start()

query.awaitTermination(30)  # Run for 30 seconds for test/demo

print(" Q12 Simulated exactly-once from Kafka to Redshift via Delta staging layer.")