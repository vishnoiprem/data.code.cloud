# Q8: Hourly aggregation and late data handling (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import window, sum, to_timestamp

spark = SparkSession.builder.appName("Q8_HourlyAggregation").getOrCreate()

from pyspark.sql import SparkSession
from pyspark.sql.functions import window, sum, to_timestamp, col

spark = SparkSession.builder.appName("Q8_HourlyAggregation").getOrCreate()

# Load data
df = spark.read.option("header", True).csv("data/transactions.csv")
df = df.withColumn("event_time", to_timestamp("event_time"))

# PySpark Way with window flattening
df_result = df.groupBy(window("event_time", "1 hour"), "branch_id") \
              .agg(sum("amount").alias("total_amount")) \
              .select(
                  col("window.start").alias("window_start"),
                  col("window.end").alias("window_end"),
                  col("branch_id"),
                  col("total_amount")
              )

# Handle late data (watermarking)
# Spark SQL Way with window flattening
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT 
        window.start AS window_start,
        window.end AS window_end,
        branch_id,
        SUM(amount) AS total_amount
    FROM (
        SELECT 
            *,
            window(to_timestamp(event_time), '1 hour') as window
        FROM transactions
    )
    GROUP BY window, branch_id
""")

# Handle late data (watermarking)
df_sql = df_sql.withWatermark("window_start", "2 hours")

df_sql.write.mode("overwrite").csv("output/q8_result_sql/")