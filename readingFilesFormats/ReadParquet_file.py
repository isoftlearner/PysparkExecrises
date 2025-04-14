from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('readingParquet').getOrCreate()
df = spark.read.parquet("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\titanic.parquet")
df.printSchema()
df.show()