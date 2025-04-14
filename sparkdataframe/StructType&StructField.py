from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
# Start Spark session
spark = SparkSession.builder.appName("StructExample").getOrCreate()
# Define schema using StructType
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("City", StringType(), True)
])
# Sample data
data = [("Alice", 25, "New York"),
        ("Bob", 30, "London"),
        ("Carol", 22, "Sydney")]
# Create DataFrame with schema
df = spark.createDataFrame(data, schema=schema)
# Show DataFrame
df.show()
