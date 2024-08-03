from pyspark.sql import Row
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example_app").getOrCreate()

unctad_data = [
    Row(year=2020, product="Fuels (SITC 3)", economy="USA", value=123.456, etl_source="unctad.csv", etl_timestamp="2021-01-01", country_iso3="USA"),
    Row(year=2020, product="Coal", economy="Canada", value=234.567, etl_source="unctad.csv", etl_timestamp="2021-01-01", country_iso3="CAN")
]
unctad_isocd_df = spark.createDataFrame(unctad_data)