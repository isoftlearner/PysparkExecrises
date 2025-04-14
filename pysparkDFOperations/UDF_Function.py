from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder \
    .appName('Dataframe_Operations') \
    .getOrCreate()

# Define the schema for our data
schema = StructType([
    StructField('Brand', StringType(), True),
    StructField('Model', StringType(), True),
    StructField('Memory', StringType(), True),
    StructField('Processor', StringType(), True),
    StructField('Price', IntegerType(), True)
])

# Create a list of tuples representing data
data = [
    ('Brand1', 'Model1', '8GB', 'Intel i5', 7000),
    ('Brand2', 'Model2', '16GB', 'Intel i7', 9000),
    ('Brand3', 'Model3', '8GB', 'AMD Ryzen 5', 6500),
    ('Brand4', 'Model4', '16GB', 'Intel i9', 12000),
    ('Brand5', 'Model5', '32GB', 'AMD Ryzen 7', 15000),
    ('Brand6', 'Model6', '16GB', 'Intel i7', 11000),
    ('Brand7', 'Model7', '8GB', 'Intel i5', 8000),
    ('Brand8', 'Model8', '16GB', 'Intel i7', 9500),
    ('Brand9', 'Model9', '32GB', 'AMD Ryzen 5', 13000),
    ('Brand10', 'Model10', '16GB', 'Intel i7', 11500)
]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()

# Print Schema
df.printSchema()

# Define your UDF function
def double_price(price):
    return price * 2

def mult(x):
    return x*2
result = lambda  x : mult(x)
print(result(2))

# Register your UDF function with DoubleType output
double_price_udf = udf(lambda price: double_price(price), IntegerType())

# Assuming 'df' is your DataFrame and 'Price' is one of the columns in df
df_udf = df.withColumn("Double_Price", double_price_udf(df["Price"]))
df_udf.show(4)
# Display the DataF