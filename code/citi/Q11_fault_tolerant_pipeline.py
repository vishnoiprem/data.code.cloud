# Q11: Fault-tolerant Spark Pipeline on AWS (PySpark + Delta Lake Simulation)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sha2, concat_ws
from delta.tables import DeltaTable
import datetime

# Initialize Spark session with Delta support
spark = SparkSession.builder \
    .appName("Q11_FaultTolerantPipeline") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Simulate raw data ingestion from S3 (here: local path)
input_path = "data/aws/trading_data_2025-07-19.csv"
output_path = "output/aws_delta/trading_data"
checkpoint_path = "output/aws_delta/_checkpoints"

# Load raw data
df = spark.read.option("header", True).csv(input_path)

# Clean & transform (cast numeric, add hash for deduplication)
df_clean = df.withColumn("amount", col("amount").cast("double")) \
             .withColumn("event_hash", sha2(concat_ws("||", *["trade_id", "timestamp"]), 256)) \
             .withColumn("processed_at", lit(datetime.datetime.now().isoformat()))

# Deduplicate by event_hash
df_dedup = df_clean.dropDuplicates(["event_hash"])

# Write to Delta Lake (simulate fault-tolerant write)
df_dedup.write.format("delta").mode("append").save(output_path)

# For production: wrap in try/except or use task retries (e.g., Airflow/Step Functions)
print(" Q11 Complete: Simulated fault-tolerant pipeline with S3 + Delta Lake.")