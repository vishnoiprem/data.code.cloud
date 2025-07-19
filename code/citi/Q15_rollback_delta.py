# Q15: Rollback last batch using Delta versioning (Concept only)

# Delta command:
# df = spark.read.format("delta").option("versionAsOf", 123).load("path")

print("Use Delta Lake time travel with 'versionAsOf' or 'timestampAsOf' for rollback.")

from delta.tables import DeltaTable

# 1. Check current version
target_path = "delta_tables/customers_dim"
delta_table = DeltaTable.forPath(spark, target_path)
latest_version = delta_table.history().selectExpr("max(version)").first()[0]
print(f"Current version: {latest_version}")

# 2. View history to find the version to roll back to
history = delta_table.history().select("version", "timestamp", "operation", "operationParameters")
history.show(truncate=False)

# 3. Roll back using RESTORE command (Delta Lake 1.0+)
version_to_restore = 123  # Replace with actual version number
delta_table.restoreToVersion(version_to_restore)

# Alternative method: Manual overwrite
# df_previous = spark.read.format("delta").option("versionAsOf", version_to_restore).load(target_path)
# df_previous.write.format("delta").mode("overwrite").save(target_path)

# 4. Verify rollback
restored_df = spark.read.format("delta").load(target_path)
print(f"Restored to version {version_to_restore}")
print(f"Record count: {restored_df.count()}")

# 5. Time travel query to confirm
spark.sql(f"""
    SELECT * 
    FROM delta.`{target_path}@v{version_to_restore}`
    WHERE customer_id = 'CUST123'
""").show()