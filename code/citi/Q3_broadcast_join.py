# Q3: Join a large transactions table with a small customer table using broadcast join (PySpark + Spark SQL)

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, sum, col

spark = SparkSession.builder.appName("Q3_BroadcastJoin").getOrCreate()
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "100MB")
spark.conf.set("spark.sql.join.preferSortMergeJoin", "false")


# Load data
df_transactions = spark.read.option("header", True).csv("data/transactions.csv")
df_customers = spark.read.option("header", True).csv("data/customers.csv")
# PySpark Way
df_joined = df_transactions.join(broadcast(df_customers), "customer_id", "left")
df_joined.write.mode("overwrite").csv("output/q3_result/")

# Spark SQL Way
df_transactions.createOrReplaceTempView("transactions")
df_customers.createOrReplaceTempView("customers")

df_sql = spark.sql("""
    SELECT t.*, c.customer_id as customer_ids,c.name,c.email
    FROM transactions as t LEFT JOIN customers as c
    ON t.customer_id = c.customer_id
""")
df_sql.write.mode("overwrite").csv("output/q3_result_sql/")