from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Create Spark session
spark = SparkSession.builder \
    .appName("Cache vs Persist Example") \
    .getOrCreate()

parquet_df = spark.write.parquet("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\Filieformats\\users.parquet")
parquet_df.show(truncate=False)

orc_df = spark.read.orc("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\Filieformats\\users.orc")
orc_df.show(truncate=False)

'''spark1 = SparkSession.builder \
    .appName("Read XML") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.15.0") \
    .getOrCreate()
xml_df = spark1.read.format('xml').load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\Filieformats\\people.xml")
xml_df.show(truncate=False)'''
