from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.appName("InnerJoinExample").getOrCreate()
# Create the first dataframe
df = spark.createDataFrame([("A", 1), ("B", 2), ("C", 3),("A",8)], ["letter", "number"])
df.show(truncate=False)

df1 = df.alias("df100")
df2 = df.alias("df200")

#df1.join(df2, df1['letter'] == df2['letter'], 'outer').show(truncate=False)

self_join = df1.join(df2, df1['letter'] == df2['letter'])

self_join.show(truncate=False)

