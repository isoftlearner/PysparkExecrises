from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
# Initialize SparkSession
spark = SparkSession.builder.appName('ProvideSchemaExample').getOrCreate()


# Define the schema: column names and their types
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Salary", IntegerType(), True)
])
# Read the CSV file with the provided schema
df = spark.read.csv("path/to/people.csv", header=True, schema=schema)

# Show the DataFrame
df.show()