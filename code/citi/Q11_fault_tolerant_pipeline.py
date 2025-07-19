# Q11: Fault-tolerant Spark pipeline on AWS (Guidance only)

# Solution:
# - Store raw data in S3
# - Use Spark on EMR or Glue
# - Use Delta Lake for ACID
# - Airflow or Step Functions for orchestration
# - Monitor with CloudWatch/Datadog
print("Design includes S3 + EMR + Delta + Airflow with retries and monitoring.")