# Q4: Handle schema changes in a nightly data pipeline (PySpark + Spark SQL)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Q4_SchemaChange").getOrCreate()

# PySpark Way
df = spark.read.option("mergeSchema", "true").parquet("data/parquet_transactions/")
df.write.mode("overwrite").parquet("output/q4_result/")

# Spark SQL Way
df.createOrReplaceTempView("transactions_parquet")
df_sql = spark.sql("SELECT * FROM transactions_parquet")
df_sql.write.mode("overwrite").parquet("output/q4_result_sql/")