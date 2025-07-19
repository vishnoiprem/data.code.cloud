
# PySpark Interview Questions - Local Execution Script (Q1 to Q15)
# Assumption: Input data is stored in local filesystem in folder 'data/' (e.g., ./data/transactions.csv)

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("InterviewQuestions").getOrCreate()

# Q1: Process millions of transactions and handle skew
df1 = spark.read.option("header", True).csv("data/transactions.csv")
df1 = df1.withColumn("salt", when(col("branch_id") == "BRANCH_001", (rand() * 10).cast("int")).otherwise(0))
df1 = df1.repartition("branch_id", "salt")
df1_clean = df1.dropna(subset=["transaction_id", "amount"]).withColumn("processing_date", lit("2025-07-18"))
df1_clean.write.mode("overwrite").partitionBy("branch_id").parquet("output/cleaned_transactions/")

# Q2: Clean nulls in transaction_type
df2 = spark.read.option("header", True).csv("data/transactions.csv")
df2 = df2.withColumn("transaction_type", when(col("transaction_type").isNull(), "UNKNOWN").otherwise(col("transaction_type")))

# Q3: Broadcast join with customer table
df_transactions = spark.read.option("header", True).csv("data/transactions.csv")
df_customers = spark.read.option("header", True).csv("data/customers.csv")
df_joined = df_transactions.join(broadcast(df_customers), "customer_id", "left")

# Q4: Handle schema changes
df4 = spark.read.option("mergeSchema", "true").parquet("data/parquet_transactions/")

# Q5: OOM debug strategy - no direct code, tuning parameters and logic

# Q6: Mask SSN
df6 = spark.read.option("header", True).csv("data/transactions.csv")
df6 = df6.withColumn("ssn_masked", sha2(col("ssn").cast("string"), 256)).drop("ssn")

# Q7: Remove duplicates
df7 = spark.read.option("header", True).csv("data/transactions.csv")
df7 = df7.dropDuplicates(["transaction_id", "processing_date"])

# Q8: Hourly aggregation and late events (Assuming streaming for event_time)
# For batch simulation
df8 = spark.read.option("header", True).csv("data/transactions.csv")
df8 = df8.withColumn("event_time", to_timestamp("event_time"))
df8_result = df8.groupBy(window("event_time", "1 hour"), "branch_id").agg(sum("amount").alias("total_amount"))

# Q9: Join + Aggregation Optimization - guidance, not direct code

# Q10: SCD Type 2 logic - usually Delta merge statement, no sample run here

# Q11: AWS pipeline guidance - no local code

# Q12: Kafka to Redshift - no local simulation

# Q13: Missing folder handling
try:
    df13 = spark.read.option("header", True).csv("data/branch_*")
except Exception as e:
    print("Skipping missing folder error:", str(e))

# Q14: Summary report
df14 = spark.read.option("header", True).csv("data/transactions.csv")
df14.groupBy("branch_id", "account_type").agg(sum("amount").alias("daily_total")).show()

# Q15: Rollback using Delta versioning - requires Delta setup
