from pyspark.sql import SparkSession
from pyspark.sql.functions import explode_outer
# Initialize Spark session
spark = SparkSession.builder.master("local").appName("explode_outer Example").getOrCreate()
# Sample data: each person has a list of fruits
data = [
    (1, ["apple", "banana", "cherry"]),  # Person 1 has fruits
    (2, ["dog", "elephant"]),  # Person 2 has fruits
    (3, []),  # Person 3 has an empty list of fruits
    (4, None)  # Person 4 has null (no fruits)
]
# Define columns for the DataFrame
columns = ["id", "fruits"]
# Create DataFrame
df = spark.createDataFrame(data, columns)
# Show the DataFrame
df.show(truncate=False)

df_exploded = df.select("id", explode_outer("fruits").alias("fruit"))
# Show the exploded DataFrame
df_exploded.show(truncate=False)
