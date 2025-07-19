# Q5: Debugging out-of-memory issues (Guidance only)

# Key PySpark tuning strategies (Not full code):
# - Use df.repartition() to increase partitions
# - Avoid wide transformations and unnecessary .cache()
# - Use df.persist(StorageLevel.DISK_ONLY)
# - Set spark.sql.shuffle.partitions to a tuned value
# - Select only required columns early: df.select("col1", "col2")

print("Refer to the job logs, Spark UI, and tweak configuration.")