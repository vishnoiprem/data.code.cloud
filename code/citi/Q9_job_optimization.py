# Q9: PySpark Optimization Techniques (Full Code + Best Practices)

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, col
from pyspark import StorageLevel

spark = SparkSession.builder.appName("Q9_OptimizationTechniques").getOrCreate()

# 1 Load data
df = spark.read.option("header", True).csv("data/transactions.csv")
df_customers = spark.read.option("header", True).csv("data/customers.csv")

# 2 Push filters early — reduce data as early as possible
df_filtered = df.filter(col("amount") > 100)

# 3⃣ Drop unused columns
df_filtered = df_filtered.select("transaction_id", "customer_id", "amount")

# 4⃣ Repartition before join/aggregation (distribute load)
df_filtered = df_filtered.repartition("customer_id")

# 5 Broadcast join with small dimension table
df_joined = df_filtered.join(broadcast(df_customers), "customer_id", "left")

# 6 Persist if reused downstream
df_joined = df_joined.persist(StorageLevel.MEMORY_AND_DISK)

# 7 Sample transformation: Aggregation
df_agg = df_joined.groupBy("customer_id").sum("amount")

#  8⃣ Write optimized result
df_agg.write.mode("overwrite").csv("output/q9_result/")

#  Optimization Summary
print("\ Q9 Complete: Applied best practices — filter pushdown, projection, broadcast join, partitioning, and persistence.")
