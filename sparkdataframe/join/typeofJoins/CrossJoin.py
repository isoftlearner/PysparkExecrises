from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("CrossJoinExample").getOrCreate()

# Create the first dataframe
df1 = spark.createDataFrame([("A", 1), ("B", 2), ("C", 3)], ["letter", "number"])

# Create the second dataframe
df2 = spark.createDataFrame([("X", 4), ("Y", 5), ("Z", 6)], ["symbol", "value"])

# Perform the cross join
cross_join = df1.crossJoin(df2)

# Show the result of the join
cross_join.show()
