import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, StringType, DoubleType, BooleanType

spark = SparkSession.builder.appName('csv file').getOrCreate()
'''df = spark.read.csv("C:\\Users\\Sunil Setty\\Desktop\\temp1\\zipcodes.csv")
df.printSchema()
df.show(truncate=False)
print("---------------------Using the path variable in the below--------")
path="C:\\Users\\Sunil Setty\\Desktop\\temp1\\zipcodes.csv"
df = spark.read.csv(path)
df.printSchema()
df.show(truncate=False)
print(df.count())'''

'''df3 = spark.read.options(header='True', delimiter=',') \
    .csv("C:\\Users\\Sunil Setty\\Desktop\\temp1\\zipcodes.csv")
df3.printSchema()'''
# Fix NativeIO Error


schema = StructType() \
    .add("RecordNumber", IntegerType(), True) \
    .add("Zipcode", IntegerType(), True) \
    .add("ZipCodeType", StringType(), True) \
    .add("City", StringType(), True) \
    .add("State", StringType(), True) \
    .add("LocationType", StringType(), True) \
    .add("Lat", DoubleType(), True) \
    .add("Long", DoubleType(), True) \
    .add("Xaxis", IntegerType(), True) \
    .add("Yaxis", DoubleType(), True) \
    .add("Zaxis", DoubleType(), True) \
    .add("WorldRegion", StringType(), True) \
    .add("Country", StringType(), True) \
    .add("LocationText", StringType(), True) \
    .add("Location", StringType(), True) \
    .add("Decommisioned", BooleanType(), True) \
    .add("TaxReturnsFiled", StringType(), True) \
    .add("EstimatedPopulation", IntegerType(), True) \
    .add("TotalWages", IntegerType(), True) \
    .add("Notes", StringType(), True)

df_with_schema = spark.read.format("csv") \
    .option("header", True) \
    .load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcodes.csv")
df_with_schema.printSchema()
df_with_schema.show()
print(df_with_schema.describe())
df_with_schema.write.partitionBy("LocationType").mode("overwrite") \
   .csv("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\outpufiles\\zipcodes.csv")

