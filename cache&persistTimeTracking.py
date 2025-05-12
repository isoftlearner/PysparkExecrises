import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark import StorageLevel

# Step 1: Create Spark session
spark = SparkSession.builder \
    .appName("Cache vs Persist Performance Example") \
    .getOrCreate()

# Step 2: Sample data
data = [("Alice", 34, "Sales"),
        ("Bob", 45, "Sales"),
        ("Charlie", 29, "Engineering"),
        ("David", 40, "Engineering"),
        ("Eve", 35, "HR"),
        ("Frank", 50, "Engineering"),
        ("Grace", 28, "Sales"),
        ("Heidi", 32, "HR"),
        ("Ivan", 39, "Sales"),
        ("Judy", 41, "HR")]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age", "Dept"])

# Step 3: Filter DataFrame
df_filtered = df.filter(col("Age") > 30)
input("show spark UI")

start_time = time.time()
count_result = df_filtered.collect()
print(f"\n[Action 1] Count result: {count_result}")
print(f"Time taken for collect(): {time.time() - start_time:.4f} seconds")

start_time = time.time()
count_result = df_filtered.count()
print(f"\n[Action 1] Count result: {count_result}")
print(f"Time taken for count: {time.time() - start_time:.4f} seconds")

# Step 6: Second operation - Group by Department and get average age
start_time = time.time()
avg_age_df = df_filtered.groupBy("Dept").agg(avg("Age").alias("AvgAge"))
avg_age_df.show()
print(f"Time taken for groupBy + agg: {time.time() - start_time:.4f} seconds")

# Step 7: Third operation - Select and show
start_time = time.time()
df_filtered.select("Name", "Age").show()
print(f"Time taken for select and show: {time.time() - start_time:.4f} seconds")
input("show SPARK UI")
print("*************************************Before cache above one **********************************************")
# Step 4: Cache or Persist the filtered data
# You can use either .cache() or .persist(StorageLevel.MEMORY_AND_DISK)
df_filtered.cache()  # or use: df_filtered.persist(StorageLevel.MEMORY_AND_DISK)

# Step 5: Track performance for first action
start_time = time.time()
count_result = df_filtered.count()
print(f"\n[Action 1] Count result: {count_result}")
print(f"Time taken for count: {time.time() - start_time:.4f} seconds")

# Step 6: Second operation - Group by Department and get average age
start_time = time.time()
avg_age_df = df_filtered.groupBy("Dept").agg(avg("Age").alias("AvgAge"))
avg_age_df.show()
print(f"Time taken for groupBy + agg: {time.time() - start_time:.4f} seconds")

# Step 7: Third operation - Select and show
start_time = time.time()
df_filtered.select("Name", "Age").show()
print(f"Time taken for select and show: {time.time() - start_time:.4f} seconds")
input("show SPARK UI")
# Optional: Unpersist the cached data
#df_filtered.unpersist()
