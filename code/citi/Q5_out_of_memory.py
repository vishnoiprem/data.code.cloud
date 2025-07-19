# Q5: Debugging out-of-memory issues (PySpark Guidance + Sample Code)

from pyspark.sql import SparkSession
from pyspark import StorageLevel
from pyspark.sql.functions import broadcast, col
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("Q5_OutOfMemoryDebugging").getOrCreate()

# Simulated DataFrame (normally you'd load a large dataset here)
df = spark.read.option("header", True).csv("data/transactions.csv")

# 1️1.Repartition to balance data across executors
df = df.repartition(200)  # Adjust based on data size and cluster

# 2.Column pruning: select only needed columns
df = df.select("transaction_id", "branch_id", "amount", "customer_id")
df = df.withColumn("amount", col("amount").cast(DoubleType()))

# 3.Avoid unnecessary caching (only use if reused multiple times)
# Incorrect: df.cache()
# Better:
df = df.persist(StorageLevel.DISK_ONLY)

# 4.Tuning shuffle partitions
spark.conf.set("spark.sql.shuffle.partitions", "100")

# 5.Sample optimization with join
df_customers = spark.read.option("header", True).csv("data/customers.csv")
df_joined = df.join(broadcast(df_customers), "customer_id", "left")

# 6 Sample transformation (e.g., aggregation)
df_result = df_joined.groupBy("branch_id").sum("amount")

# 7. write output (simulate job completion)
df_result.write.mode("overwrite").csv("output/q5_result/")

print("Q5: OOM prevention strategies applied - repartitioned, pruned, persisted, and joined efficiently.")