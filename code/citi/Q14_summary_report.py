# Q14: Daily summary report (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("Q14_SummaryReport").getOrCreate()

# PySpark Way
df = spark.read.option("header", True).csv("data/transactions.csv")
df.groupBy("branch_id", "account_type").agg(sum("amount").alias("daily_total"))   .write.mode("overwrite").parquet("output/q14_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT branch_id, account_type, SUM(amount) AS daily_total
    FROM transactions
    GROUP BY branch_id, account_type
""")
df_sql.write.mode("overwrite").parquet("output/q14_result_sql/")