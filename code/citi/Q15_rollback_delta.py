# Q15: Rollback last batch using Delta versioning (Concept only)

# Delta command:
# df = spark.read.format("delta").option("versionAsOf", 123).load("path")

print("Use Delta Lake time travel with 'versionAsOf' or 'timestampAsOf' for rollback.")