# Q3: Join a large transactions table with a small customer table using broadcast join (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder.appName("Q3_BroadcastJoin").getOrCreate()

# Load data
df_transactions = spark.read.option("header", True).csv("data/transactions.csv")
df_customers = spark.read.option("header", True).csv("data/customers.csv")

# PySpark Way
df_joined = df_transactions.join(broadcast(df_customers), "customer_id", "left")
df_joined.write.mode("overwrite").parquet("output/q3_result/")

# Spark SQL Way
df_transactions.createOrReplaceTempView("transactions")
df_customers.createOrReplaceTempView("customers")

df_sql = spark.sql("""
    SELECT *
    FROM transactions LEFT JOIN customers
    ON transactions.customer_id = customers.customer_id
""")
df_sql.write.mode("overwrite").parquet("output/q3_result_sql/")