# Q7: Remove duplicates in output file (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Q7_RemoveDuplicates").getOrCreate()

# PySpark Way
df = spark.read.option("header", True).csv("data/transactions.csv")
df_dedup = df.dropDuplicates(["transaction_id", "processing_date"])
df_dedup.write.mode("overwrite").parquet("output/q7_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (PARTITION BY transaction_id, processing_date ORDER BY transaction_id) AS rn
        FROM transactions
    ) WHERE rn = 1
""")
df_sql.write.mode("overwrite").parquet("output/q7_result_sql/")