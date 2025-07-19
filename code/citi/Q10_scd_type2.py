# Q10: SCD Type 2 Implementation (Delta Lake required - Concept only)

# Conceptual SQL/Delta Merge for SCD Type 2
# MERGE INTO target_table USING source_table
# ON target.id = source.id AND target.current_flag = true
# WHEN MATCHED AND target.hash != source.hash THEN
#   UPDATE SET current_flag = false, end_date = source.start_date
# WHEN NOT MATCHED THEN
#   INSERT (columns...) VALUES (values...)

print("Use Delta merge operation for SCD Type 2, with hash comparison or field tracking.")

from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws, lit, current_timestamp

# Enable Delta Lake extensions
spark = SparkSession.builder \
    .appName("Q10_SCDType2_Delta") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Existing Delta table (historical records)
df_existing = spark.createDataFrame([
    (1, "John", "ACTIVE", "2023-01-01", None, True, "oldhash"),
], ["customer_id", "name", "status", "start_date", "end_date", "current_flag", "record_hash"])

df_existing.write.format("delta").mode("overwrite").save("output/scd_target")

# New incoming data (changes and new records)
df_new = spark.createDataFrame([
    (1, "John", "INACTIVE", "2025-07-19"),  # Status changed
    (2, "Jane", "ACTIVE", "2025-07-19"),    # New record
], ["customer_id", "name", "status", "start_date"])

# Add hash to detect change
df_new = df_new.withColumn("record_hash", sha2(concat_ws("||", *["customer_id", "name", "status"]), 256)) \
               .withColumn("current_flag", lit(True)) \
               .withColumn("end_date", lit(None).cast("string"))

# Perform SCD Type 2 Merge
from delta.tables import DeltaTable

delta_target = DeltaTable.forPath(spark, "output/scd_target")

delta_target.alias("target").merge(
    df_new.alias("source"),
    "target.customer_id = source.customer_id AND target.current_flag = true"
).whenMatchedUpdate(
    condition="target.record_hash != source.record_hash",
    set={
        "current_flag": "false",
        "end_date": "current_timestamp()"
    }
).whenNotMatchedInsert(
    values={
        "customer_id": "source.customer_id",
        "name": "source.name",
        "status": "source.status",
        "start_date": "source.start_date",
        "end_date": "source.end_date",
        "current_flag": "source.current_flag",
        "record_hash": "source.record_hash"
    }
).execute()

print("Q10: SCD Type 2 merge completed with Delta Lake.")
