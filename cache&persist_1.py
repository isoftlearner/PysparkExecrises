import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark import StorageLevel

# Step 1: Create SparkSession
spark = SparkSession.builder.appName("Persist Performance Example").getOrCreate()

# Step 2: Sample data
data = [
    ("Alice", 34, "Sales"),
    ("Bob", 45, "Sales"),
    ("Charlie", 29, "Engineering"),
    ("David", 40, "Engineering"),
    ("Eve", 35, "HR"),
    ("Frank", 50, "Engineering"),
    ("Grace", 28, "Sales"),
    ("Heidi", 32, "HR"),
    ("Ivan", 39, "Sales"),
    ("Judy", 41, "HR")
]

# Step 3: Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "Dept"])

# Step 4: Filter DataFrame
df_filtered = df.filter(col("Age") > 30)

# Step 5: Persist using MEMORY_AND_DISK
df_filtered.persist(StorageLevel.MEMORY_AND_DISK)

# Step 6: First action - Count
start_time = time.time()
count_result = df_filtered.count()
print(f"\n[Action 1] Count: {count_result}")
print(f"Time taken for count: {time.time() - start_time:.4f} seconds")

# Step 7: Second action - Average Age per Department
start_time = time.time()
avg_age_df = df_filtered.groupBy("Dept").agg(avg("Age").alias("AvgAge"))
avg_age_df.show()
print(f"Time taken for groupBy + avg: {time.time() - start_time:.4f} seconds")

# Step 8: Third action - Display names and age
start_time = time.time()
df_filtered.select("Name", "Age").show()
print(f"Time taken for select and show: {time.time() - start_time:.4f} seconds")

# Step 9: Unpersist
df_filtered.unpersist()
