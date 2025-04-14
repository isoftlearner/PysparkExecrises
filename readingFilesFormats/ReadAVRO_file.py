from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('readingParquet').getOrCreate()
df = spark.read.format("avro").load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\userdata5.avro")
df.printSchema()
df.show()