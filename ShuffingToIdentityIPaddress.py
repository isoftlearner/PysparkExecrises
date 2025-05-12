from pyspark.sql import SparkSession
import socket

# Create Spark session
spark = SparkSession.builder \
    .appName("ShuffleExecutorExample") \
    .master("l[2]ocal") \
    .getOrCreate()

sc = spark.sparkContext

# Sample transaction data
transactions_data = [
    (1, "Ahmed", 100, "2022-01-01"),
    (2, "John", 200, "2022-01-02"),
    (3, "Fabrice", 300, "2022-01-03"),
    (4, "Mehdi", 400, "2022-01-04"),
    (5, "Mehdi", 500, "2022-01-05")
]

customers_data = [
    ("Ahmed", "Morocco"),
    ("John", "USA"),
    ("Fabrice", "France"),
    ("Mehdi", "Algeria")
]

# Create DataFrames
transactions_df = spark.createDataFrame(transactions_data, ["id", "customer", "amount", "order_date"])
customers_df = spark.createDataFrame(customers_data, ["customer", "country"])

# Convert DataFrame to RDD to inspect partition data
def partition_info(index, iterator):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return [(index, host, ip, list(iterator))]

# BEFORE SHUFFLE: see where transaction records are
print("=== Before Shuffle ===")
transactions_rdd = transactions_df.rdd.mapPartitionsWithIndex(partition_info)
for part in transactions_rdd.collect():
    print(f"Partition {part[0]} on host {part[1]} (IP: {part[2]}) has data: {part[3]}")

# GROUP BY: causes shuffle
grouped_df = transactions_df.groupBy("customer").sum("amount")

# AFTER SHUFFLE (groupBy)
print("\n=== After groupBy (Shuffling) ===")
grouped_rdd = grouped_df.rdd.mapPartitionsWithIndex(partition_info)
for part in grouped_rdd.collect():
    print(f"Partition {part[0]} on host {part[1]} (IP: {part[2]}) has data: {part[3]}")

# JOIN: causes another shuffle unless one side is broadcast
joined_df = grouped_df.join(customers_df, on="customer", how="inner")

# AFTER JOIN (Shuffling again)
print("\n=== After join (Shuffling again) ===")
joined_rdd = joined_df.rdd.mapPartitionsWithIndex(partition_info)
for part in joined_rdd.collect():
    print(f"Partition {part[0]} on host {part[1]} (IP: {part[2]}) has data: {part[3]}")
