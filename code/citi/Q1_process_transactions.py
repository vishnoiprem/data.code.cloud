# Q1: Process millions of transactions from 30+ branches and handle skew (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, rand, lit

spark = SparkSession.builder.appName("Q1_ProcessTransactions").getOrCreate()

# Load data
df = spark.read.option("header", True).csv("data/transactions.csv")

# PySpark Way
df_salted = df.withColumn("salt", when(col("branch_id") == "BRANCH_001", (rand() * 10).cast("int")).otherwise(0))
df_salted = df_salted.repartition("branch_id", "salt")
df_clean = df_salted.dropna(subset=["transaction_id", "amount"]).withColumn("processing_date", lit("2025-07-18"))
df_clean.write.mode("overwrite").partitionBy("branch_id").csv("output/q1_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

spark.sql("""
    CREATE OR REPLACE TEMP VIEW transactions_salted AS
    SELECT *,
           CASE WHEN branch_id = 'BRANCH_001' THEN CAST(rand() * 10 AS INT) ELSE 0 END AS salt
    FROM transactions
""")
df_sql = spark.sql("""
    SELECT *,
           '2025-07-18' AS processing_date
    FROM transactions_salted
    WHERE transaction_id IS NOT NULL AND amount IS NOT NULL
""")
df_sql.write.mode("overwrite").partitionBy("branch_id").csv("output/q1_result_sql/")