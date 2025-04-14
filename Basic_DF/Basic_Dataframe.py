from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName('Creating Dataframe').getOrCreate()
# List of data
data = [("John", 25), ("Sara", 30), ("Mike", 35)]

# Column names
columns = ["Name", "Age"]

# Creating DataFrame
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()
