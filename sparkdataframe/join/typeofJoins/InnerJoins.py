from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.appName("InnerJoinExample").getOrCreate()
# Create the first dataframe
df = spark.createDataFrame([("A", 1), ("B", 2), ("C", 3),("A",8)], ["letter", "number"])
df.show(truncate=False)

#df1.join(df2, df1['letter'] == df2['letter'], 'outer').show(truncate=False)

#self_join = df.alias("df100").join(df.alias("df200"), df100["letter"] == df200["letter"])

df.alias("a").join(df.alias("b"),"letter").show()

#self_join.show(truncate=False)
# Create the second dataframe
df2 = spark.createDataFrame([("A", 4), ("B", 5), ("D", 6),("B",10)], ["letter", "value"])
df2.show(truncate=False)

#df1.join(df2, df1['letter'] == df2['letter'],'crossjoin').show(truncate=False)

df.crossJoin(df2).show(truncate=False)

# Perform the inner join
#df1.join(df2, df1['letter'] == df2['letter'], 'outer').show(truncate=False)

self_join = df.alias("df100").join(df.alias("df200"), df100["letter"] == df200["letter"])

self_join.show(truncate=False)

