# Q9: PySpark Optimization Techniques (Fixed Version)

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, col
from pyspark import StorageLevel
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("Q9_OptimizationTechniques").getOrCreate()

# 1 Load data
df = spark.read.option("header", True).csv("data/transactions.csv")
df_customers = spark.read.option("header", True).csv("data/customers.csv")

# 2 Cast 'amount' to DoubleType to allow aggregation
df = df.withColumn("amount", col("amount").cast(DoubleType()))

# 3 Push filters early
df_filtered = df.filter(col("amount") > 100)

# 4 Drop unused columns
df_filtered = df_filtered.select("transaction_id", "customer_id", "amount")

# 5 Repartition to balance join/aggregation
df_filtered = df_filtered.repartition("customer_id")

# 6 Broadcast join
df_joined = df_filtered.join(broadcast(df_customers), "customer_id", "left")

# 7 Persist if reused multiple times
df_joined = df_joined.persist(StorageLevel.MEMORY_AND_DISK)

# 8 Aggregation
df_agg = df_joined.groupBy("customer_id").sum("amount")

# 9 Write result
df_agg.write.mode("overwrite").csv("output/q9_result/")

# 10 Optional: Spark SQL Version
df_filtered.createOrReplaceTempView("transactions")
df_customers.createOrReplaceTempView("customers")

df_sql = spark.sql("""
    SELECT t.customer_id, SUM(CAST(t.amount AS DOUBLE)) AS total_amount
    FROM transactions t
    LEFT JOIN customers c ON t.customer_id = c.customer_id
    WHERE CAST(t.amount AS DOUBLE) > 100
    GROUP BY t.customer_id
""")
df_sql.write.mode("overwrite").csv("output/q9_result_sql/")

print(" Q9 Complete: Optimized with cast, filter, projection, broadcast, repartition, and persistence.")