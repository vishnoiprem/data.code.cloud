# Q4: Handle schema changes in a nightly data pipeline (PySpark + Spark SQL)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Q4_SchemaChange").getOrCreate()

# PySpark Way
# df = spark.read.option("header", True).csv("data/transactions.csv")


df1 = spark.createDataFrame([
    (1, "BRANCH_001", 100.0),
    (2, "BRANCH_002", 200.0)
], ["transaction_id", "branch_id", "amount"])

df2 = spark.createDataFrame([
    (3, "BRANCH_003", 300.0, "USD"),
    (4, "BRANCH_004", 400.0, "EUR")
], ["transaction_id", "branch_id", "amount", "currency"])

df1.write.mode("overwrite").parquet("data/parquet_transactions/")
df2.write.mode("append").parquet("data/parquet_transactions/")



df = spark.read.option("mergeSchema", "true").parquet("data/parquet_transactions/")
df.printSchema()



# df = spark.read.option("mergeSchema", "true").parquet("data/parquet_transactions/")
df.write.mode("overwrite").csv("output/q4_result/")






# Spark SQL Way
df.createOrReplaceTempView("transactions_parquet")
df_sql = spark.sql("SELECT * FROM transactions_parquet")
df_sql.write.mode("overwrite").csv("output/q4_result_sql/")