from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Create Spark session
spark = SparkSession.builder \
    .appName("Cache vs Persist Example") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 34, "Sales"),
    ("Bob", 45, "Sales"),
    ("Charlie", 29, "Engineering"),
    ("David", 40, "Engineering"),
    ("Eve", 35, "HR")
]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "Dept"])

# Perform a transformation
df_filtered = df.filter(col("Age") > 30)

# CACHE: Store the filtered DataFrame in memory
df_filtered.cache()

# Operation 1: Count
print("Count:", df_filtered.count())

# Operation 2: Group By Department and average age
df_avg_age = df_filtered.groupBy("Dept").agg(avg("Age").alias("AvgAge"))
df_avg_age.show()

# Unpersist when done
df_filtered.unpersist()
