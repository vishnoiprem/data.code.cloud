# Q8: Hourly aggregation and late data handling (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import window, sum, to_timestamp

spark = SparkSession.builder.appName("Q8_HourlyAggregation").getOrCreate()

# PySpark Way
df = spark.read.option("header", True).csv("data/transactions.csv")
df = df.withColumn("event_time", to_timestamp("event_time"))
df_result = df.groupBy(window("event_time", "1 hour"), "branch_id").agg(sum("amount").alias("total_amount"))
df_result.write.mode("overwrite").parquet("output/q8_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT window, branch_id, SUM(amount) AS total_amount
    FROM (
        SELECT *, window(to_timestamp(event_time), '1 hour') as window
        FROM transactions
    )
    GROUP BY window, branch_id
""")
df_sql.write.mode("overwrite").parquet("output/q8_result_sql/")