# -*- coding: utf-8 -*-
"""
author SparkByExamples.com
"""
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType,BooleanType,DoubleType
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("Json file format") \
    .getOrCreate()

# Read JSON file into dataframe
df = spark.read.json("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcodes.json")
df.printSchema()
df.show()

# Read multiline json file
multiline_df = spark.read.option("multiline","true") \
      .json("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\multiline-zipcode.json")
multiline_df.show()

#Read multiple files
df2 = spark.read.json(
    ['E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcode2.json','E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcode1.json'])
df2.show()

#Read All JSON files from a directory
df3 = spark.read.json("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\*.json")
df3.show()

# Define custom schema
schema = StructType([
      StructField("RecordNumber",IntegerType(),True),
      StructField("Zipcode",IntegerType(),True),
      StructField("ZipCodeType",StringType(),True),
      StructField("City",StringType(),True),
      StructField("State",StringType(),True),
      StructField("LocationType",StringType(),True),
      StructField("Lat",DoubleType(),True),
      StructField("Long",DoubleType(),True),
      StructField("Xaxis",IntegerType(),True),
      StructField("Yaxis",DoubleType(),True),
      StructField("Zaxis",DoubleType(),True),
      StructField("WorldRegion",StringType(),True),
      StructField("Country",StringType(),True),
      StructField("LocationText",StringType(),True),
      StructField("Location",StringType(),True),
      StructField("Decommisioned",BooleanType(),True),
      StructField("TaxReturnsFiled",StringType(),True),
      StructField("EstimatedPopulation",IntegerType(),True),
      StructField("TotalWages",IntegerType(),True),
      StructField("Notes",StringType(),True)
  ])

df_with_schema = spark.read.schema(schema) \
        .json("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcodes.json")
df_with_schema.printSchema()
df_with_schema.show()

# Create a table from Parquet File
df = spark.read.json("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\zipcodes.json")
df.createOrReplaceTempView("zipcode3")
spark.sql("SELECT * FROM zipcode3").show()

# PySpark write Parquet File
df2.write.mode('Overwrite').json("/tmp/spark_output/zipcodes.json")