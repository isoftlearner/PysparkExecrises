from pyspark.sql import SparkSession
import socket

# Start Spark
spark = SparkSession.builder \
    .appName("ShuffleDemo") \
    .master("local[2]") \
    .getOrCreate()

sc = spark.sparkContext

# Create RDD with 2 partitions
rdd = sc.parallelize([
    ("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5), ("c", 6)
], 2)

# Function to log where data lives (partition + hostname)
def inspect_partition(index, iterator):
    host = socket.gethostname()
    yield (index, host, list(iterator))

print("=== Before Shuffle (Raw Partitions) ===")
before = rdd.mapPartitionsWithIndex(inspect_partition).collect()
for part in before:
    print(f"Partition {part[0]} on {part[1]} contains: {part[2]}")

# Perform groupBy on the key (this triggers shuffle)
grouped_rdd = rdd.groupBy(lambda x: x[0])

print("\n=== After Shuffle (Grouped by Key) ===")
after = grouped_rdd.mapPartitionsWithIndex(inspect_partition).collect()
for part in after:
    print(f"Partition {part[0]} on {part[1]} contains: {part[2]}")
