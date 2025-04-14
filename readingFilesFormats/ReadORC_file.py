from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('readingParquet').getOrCreate()
df = spark.read.format("orc").load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\sample1\\*.orc")
df.printSchema()
df.show()
df = spark.read.format("orc").load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\sample3\\*.orc")
df.printSchema()
df.show()