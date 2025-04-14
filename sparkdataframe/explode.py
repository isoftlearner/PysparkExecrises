from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
# Initialize Spark session
spark = SparkSession.builder.master("local").appName("Explode Example").getOrCreate()
# Sample data with lists in one column
data = [
    (1, ["apple", "banana", "cherry"]),
    (2, ["orange", "grape"]),
    (3, ["mango", "kiwi"])
]
# Create a DataFrame
df = spark.createDataFrame(data, ["id", "fruits"])
# Show the original DataFrame
df.show(truncate=False)
# Use explode to flatten the 'fruits' column
df_exploded = df.withColumn("fruit", explode(df["fruits"]))
# Show the exploded DataFrame
df_exploded.show(truncate=False)
