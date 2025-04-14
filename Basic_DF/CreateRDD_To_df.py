from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
# Create a SparkSession
spark = SparkSession.builder.appName('RDDtoDFExample').getOrCreate()
# Create a list of tuples
data = [("John", 25), ("Sara", 30), ("Mike", 35)]

# Create an RDD from the list
rdd = spark.sparkContext.parallelize(data)

# Define the schema for the DataFrame
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

# Convert the RDD into a DataFrame using the defined schema
df = spark.createDataFrame(rdd, schema)

# Show the DataFrame
df.show()
