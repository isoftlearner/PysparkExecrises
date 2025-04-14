from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, concat
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

#Select Specific Columns from an existing dataframe
df_selected = df.select("Brand","Processor","Price")
df_selected.show(truncate=False)

#Filtering Rows
df_filter = df.filter(df.Price > 10000)
df_filter_1 = df.filter(df['Price'] > 10000)
df_filter_2 = df.filter(col('Price') > 10000)
df_filter.show()

#Adding a new Column in existing dataframe
df_modified = df.withColumn('Discounted_Price',col('Price')*0.9)
df_modified.show()
#Add a constant column
# Add a constant column 'Warranty_Years' with value '2'
df_constant_column = df.withColumn('Warranty_Years', lit(2))
df_constant_column.show()

#Data Type of a Column

df_converted = df.withColumn("Price",df["Price"].cast("double"))

# Get data type of modified 'Price' column in df_converted dataframe
price_type = [dtype for name, dtype in df_converted.dtypes if name == 'Price'][0]
print(f"The data type of 'Price' column is {price_type}.")

# Deriving a new column from existing columns
# Concatenate 'Brand' and 'Model' columns into a new column "Full_Name"
df_concate = df.withColumn('Full_Name', concat(col('Brand'), lit(' '), col('Model')))
df_concate.show()

#Dropping a Column
df_dropped = df_concate.drop('Full_Name')
df_dropped.show()

#Describe Data
df.describe().show()

#11. Sorting rows
# Sort rows by Price in descending order
df_ordered_desc = df.orderBy(df['Price'].desc())
df_ordered_desc.show()

# Sort rows by Price in ascending order
df_ordered_asc = df.orderBy(df['Price'].asc())
df_ordered_asc.show()

#12. Grouping and Aggregating the data
from pyspark.sql.functions import avg

# Group by 'Brand' and calculate average 'Price'
df_grouped = df.groupBy('Brand').agg(avg('Price').alias('Average_Price'))
df_grouped.orderBy(df_grouped["Brand"].asc()).show()

# Joining Dataframes
brands_data = [("Brand1", "USA"), ("Brand2", "China"), ("Brand3", "USA"), ("Brand4", "Japan"), ("Brand5", "Germany")]
brands_schema = ["Brand", "Country"]
brands_df = spark.createDataFrame(brands_data, brands_schema)
brands_df.show()

#Join the DataFrames on ‘Brand’
df_joined_inner = df.join(brands_df, on='Brand', how='inner')

# Show DataFrame
df_joined_inner.show()

df_joined_left = df.join(brands_df, on='Brand', how='left')

# Show DataFrame
df_joined_left.show()