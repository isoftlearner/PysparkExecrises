from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName('InferSchemaExample').getOrCreate()
# Read CSV file into DataFrame with inferSchema enabled
df = spark.read.csv("path/to/people.csv", header=True, inferSchema=True)

# Show the DataFrame schema (column data types)
df.printSchema()

# Show first few rows of the DataFrame
df.show()