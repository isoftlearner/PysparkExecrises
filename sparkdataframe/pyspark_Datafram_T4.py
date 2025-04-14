from pyspark.sql import SparkSession

spark: SparkSession = SparkSession.builder \
    .master("local[1]") \
    .appName("Spark Class5") \
    .getOrCreate()

filePath="E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\small_zipcode.csv"

df= spark.read.options(header='true',inferschema='true').csv(filePath)

df.printSchema()
df.show()