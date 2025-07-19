# Q10: SCD Type 2 Implementation (Delta Lake required - Concept only)

# Conceptual SQL/Delta Merge for SCD Type 2
# MERGE INTO target_table USING source_table
# ON target.id = source.id AND target.current_flag = true
# WHEN MATCHED AND target.hash != source.hash THEN
#   UPDATE SET current_flag = false, end_date = source.start_date
# WHEN NOT MATCHED THEN
#   INSERT (columns...) VALUES (values...)

from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, concat_ws, lit, current_timestamp
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType
from delta.tables import DeltaTable

# Enable Delta Lake extensions
spark = SparkSession.builder \
    .appName("Q10_SCDType2_Delta") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Define schema to avoid inference issues
schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("status", StringType(), True),
    StructField("start_date", StringType(), True),
    StructField("end_date", StringType(), True),
    StructField("current_flag", BooleanType(), True),
    StructField("record_hash", StringType(), True)
])

# Historical data (Delta table)
df_existing = spark.createDataFrame([
    (1, "John", "ACTIVE", "2023-01-01", None, True, "oldhash"),
], schema=schema)

df_existing.write.format("delta").mode("overwrite").save("output/scd_target")

# New incoming data
df_new = spark.createDataFrame([
    (1, "John", "INACTIVE", "2025-07-19"),
    (2, "Jane", "ACTIVE", "2025-07-19"),
], ["customer_id", "name", "status", "start_date"])

# Add hash column, flags
df_new = df_new.withColumn("record_hash", sha2(concat_ws("||", *["customer_id", "name", "status"]), 256)) \
               .withColumn("current_flag", lit(True)) \
               .withColumn("end_date", lit(None).cast("string"))

# Save new data as temp table
df_new.createOrReplaceTempView("staging_data")

# SQL VIEW: Historical table
spark.read.format("delta").load("output/scd_target").createOrReplaceTempView("scd_target")

# Optional SQL query to view changes
spark.sql("""
    SELECT t.customer_id, t.name, t.status, t.start_date, t.end_date, t.current_flag, t.record_hash
    FROM scd_target t
""").show()

# Perform SCD Type 2 Delta merge
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

print(" Q10: SCD Type 2 Delta Lake with SQL View completed.")