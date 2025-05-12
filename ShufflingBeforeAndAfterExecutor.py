from pyspark.sql import SparkSession
import socket

# Start Spark session with multiple cores (simulating parallelism)
spark = SparkSession.builder.appName("ShuffleExecutorCoreTrace").master("local[4]")   # Use 4 cores to simulate multiple executors.config("spark.sql.shuffle.partitions", "4") .getOrCreate()

sc = spark.sparkContext

# Sample sales data
transactions = [
    (1, "Alice", 100, "2024-01-01"),
    (2, "Bob", 200, "2024-01-02"),
    (3, "Alice", 150, "2024-01-03"),
    (4, "David", 300, "2024-01-04"),
    (5, "Bob", 250, "2024-01-05"),
    (6, "Eve", 400, "2024-01-06"),
    (7, "David", 500, "2024-01-07")
]

customers = [
    ("Alice", "USA"),
    ("Bob", "UK"),
    ("David", "Germany"),
    ("Eve", "France")
]

# Create DataFrames
tx_df = spark.createDataFrame(transactions, ["id", "customer", "amount", "order_date"])
cust_df = spark.createDataFrame(customers, ["customer", "country"])

# Function to log partition data with host & IP
def log_partition_info(index, iterator):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return [(index, host, ip, list(iterator))]

# Show partition info before shuffle
print("=== BEFORE SHUFFLE ===")
tx_df.rdd.mapPartitionsWithIndex(log_partition_info).collect()
before = tx_df.rdd.mapPartitionsWithIndex(log_partition_info).collect()
for part in before:
    print(f"Partition {part[0]} handled by host {part[1]} (IP: {part[2]}) has data: {part[3]}")

# Shuffle: groupBy causes shuffle
grouped_df = tx_df.groupBy("customer").sum("amount")

print("\n=== AFTER groupBy SHUFFLE ===")
after_groupby = grouped_df.rdd.mapPartitionsWithIndex(log_partition_info).collect()
for part in after_groupby:
    print(f"Partition {part[0]} handled by host {part[1]} (IP: {part[2]}) has data: {part[3]}")

# Another shuffle: join with customer info
joined_df = grouped_df.join(cust_df, on="customer", how="inner")

print("\n=== AFTER JOIN SHUFFLE ===")
after_join = joined_df.rdd.mapPartitionsWithIndex(log_partition_info).collect()
for part in after_join:
    print(f"Partition {part[0]} handled by host {part[1]} (IP: {part[2]}) has data: {part[3]}")

# Force another shuffle by repartitioning
repartitioned = joined_df.repartition(2)

print("\n=== AFTER REPARTITION (New Shuffle) ===")
after_repartition = repartitioned.rdd.mapPartitionsWithIndex(log_partition_info).collect()
for part in after_repartition:
    print(f"Partition {part[0]} handled by host {part[1]} (IP: {part[2]}) has data: {part[3]}")
