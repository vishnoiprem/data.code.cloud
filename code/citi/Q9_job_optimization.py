# Q9: Optimization techniques (Guidance only)

# Key PySpark strategies:
# - Use broadcast joins for small dimension tables
# - Push filters early
# - Drop unused columns with select()
# - Repartition before joins or aggregations
# - Use cache() or persist() only when reused

print("Focus on partitioning, pruning, broadcast joins, and caching selectively.")