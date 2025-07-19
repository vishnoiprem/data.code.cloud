# Q6: Mask SSN before loading to a data lake (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

spark = SparkSession.builder.appName("Q6_MaskSSN").getOrCreate()

# PySpark Way
df = spark.read.option("header", True).csv("data/transactions.csv")
df_masked = df.withColumn("ssn_masked", sha2(col("ssn").cast("string"), 256)).drop("ssn")
df_masked.write.mode("overwrite").csv("output/q6_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions")

df_sql = spark.sql("""
    SELECT transaction_id, amount, branch_id, event_time, transaction_type,
           customer_id, account_type,
           sha2(CAST(ssn AS STRING), 256) AS ssn_masked
    FROM transactions
""")
df_sql.write.mode("overwrite").csv("output/q6_result_sql/")