from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import expr
import logging

# Initialize Spark Session
spark = SparkSession.builder.appName("example_app").getOrCreate()

# Create sample DataFrame
data = [
    Row(Country="USA", Product="Oil", Q1=123.456, Q2=789.123, Q3=456.789),
    Row(Country="Canada", Product="Gas", Q1=234.567, Q2=890.234, Q3=567.890),
    Row(Country="Mexico", Product="Coal", Q1=345.678, Q2=901.345, Q3=678.901)
]
columns = ["Country", "Product", "Q1", "Q2", "Q3"]
df = spark.createDataFrame(data)

# Show original DataFrame
print("Original DataFrame:")
df.show()

# Logger setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Define the unpivot function
def unpivot_source_data(source_data_df, unpivot_cols, source_df_name):
    logger.info("Unpivot started")
    try:
        wo_unpivot_cols = [col for col in source_data_df.columns if col not in unpivot_cols]
        expr_str = ""
        for col in unpivot_cols:
            expr_str += f"'{col}', {col},"
        expr_str = expr_str[:-1] if expr_str else expr_str
        unpivot_expr = f"stack({len(unpivot_cols)},{expr_str}) as (metric, value)"
        unpivoted_df = source_data_df.selectExpr(*wo_unpivot_cols, unpivot_expr)
        logger.info("Unpivot completed")
        return unpivoted_df
    except Exception as err:
        logger.error(f"Unpivot failed with :{err}")
        raise Exception(f"Unpivot failed with :{err}")

# Define the columns to unpivot
unpivot_cols = ["Q1", "Q2", "Q3"]

# Unpivot the DataFrame
unpivoted_df = unpivot_source_data(df, unpivot_cols, "example_df")

# Show the result
print("Unpivoted DataFrame:")
unpivoted_df.show()