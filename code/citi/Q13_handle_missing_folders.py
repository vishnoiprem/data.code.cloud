# Q13: Handle missing folders in S3 (PySpark + Spark SQL)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Q13_HandleMissingFolders").getOrCreate()

try:
    df = spark.read.option("header", True).csv("data/branch_*")
    df.write.mode("overwrite").csv("output/q13_result/")
except Exception as e:
    print("Missing folders skipped:", e)