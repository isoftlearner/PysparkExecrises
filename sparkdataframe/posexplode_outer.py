from pyspark.sql import SparkSession
from pyspark.sql.functions import posexplode_outer
# Initialize Spark session
spark = SparkSession.builder.master("local").appName("posexplode_outer Example").getOrCreate()
# Sample data with arrays, including an empty array
data = [
    (1, ["apple", "banana", "cherry"]),
    (2, ["orange", "grape"]),
    (3, []),  # Empty array
    (4, None)  # Null array
]
# Create a DataFrame
df = spark.createDataFrame(data, ["id", "fruits"])
# Show the original DataFrame
df.show(truncate=False)
# Use posexplode_outer to explode and keep the position
df_exploded = df.withColumn("pos_fruit", posexplode_outer(df["fruits"]))
# Show the exploded DataFrame
df_exploded.show(truncate=False)
