# Q2: Clean null values in transaction_type without losing critical records (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("Q2_CleanTransactionType").getOrCreate()

# Load data
df = spark.read.option("header", True).csv("data/transactions.csv")

# PySpark Way
df_cleaned = df.withColumn("transaction_type", when(col("transaction_type").isNull(), "UNKNOWN").otherwise(col("transaction_type")))
df_cleaned.write.mode("overwrite").csv("output/q2_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT *,
           CASE WHEN coalesce( transaction_type,"")="" THEN 'UNKNOWN' ELSE transaction_type END AS transaction_type_fixed
    FROM transactions
""")
df_sql.write.mode("overwrite").csv("output/q2_result_sql/")