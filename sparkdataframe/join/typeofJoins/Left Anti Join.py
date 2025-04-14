from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.appName("LeftAntiJoinExample").getOrCreate()
# Create the first dataframe
df1 = spark.createDataFrame([("A", 1), ("B", 2), ("C", 3)], ["letter", "number"])
df1.show(truncate=False)
# Create the second dataframe
df2 = spark.createDataFrame([("A", 4), ("B", 5)], ["letter", "value"])
df2.show(truncate=False)
# Perform the left anti join
left_anti_join = df1.join(df2, df1['letter'] == df2['letter'], "left_anti")
left_anti_join.show(truncate=False)
# Show the result of the join
left_anti_join.show()

# Output:
# +-----+------+
# |letter|number|
# +-----+------+
# |    C|     3|
# +-----+------+