from pyspark import SparkContext

sc = SparkContext("local", "shufflingDemo")

# Create an RDD with 2 partitions
rdd = sc.parallelize([("a", 1), ("b", 2), ("a", 3), ("b", 4)],2)
print(rdd.getNumPartitions())
# Show how data is split across partitions
print("Before groupBy:")
print(rdd.glom().collect())

# groupBy on the key (x[0])
grouped = rdd.groupBy(lambda x: x[0])
print(grouped.getNumPartitions())
# Convert grouped data into readable format
print("\nAfter groupBy:")
print([(k, list(v)) for k, v in grouped.collect()])
input("spark UI look up:")
