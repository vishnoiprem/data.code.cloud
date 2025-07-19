# Q7: Remove duplicates in output file (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Q7_RemoveDuplicates").getOrCreate()

# PySpark Way
df = spark.read.option("header", True).csv("data/transactions.csv")
df_dedup = df.dropDuplicates(["transaction_id", "event_time"])
df_dedup.write.mode("overwrite").csv("output/q7_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY transaction_id, event_time  ORDER BY transaction_id DESC ) AS rn
        FROM transactions
    ) WHERE rn = 1
""")
df_sql.write.mode("overwrite").csv("output/q7_result_sql/")