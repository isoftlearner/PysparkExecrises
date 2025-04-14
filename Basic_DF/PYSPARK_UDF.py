from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
# Initialize Spark session
spark = SparkSession.builder.appName('UDFExample').getOrCreate()
# Sample data
data = [("John", 25), ("Sara", 30), ("Mike", 35)]
# Column names
columns = ["Name", "Age"]
# Create DataFrame
df = spark.createDataFrame(data, columns)
# Show the DataFrame
df.show()

def add_five_years(age):
    return age + 5

# Register the function as a UDF
add_five_years_udf = udf(add_five_years, IntegerType())

# Apply the UDF to the DataFrame
df_with_new_age = df.withColumn("AgePlusFive", add_five_years_udf(df["Age"]))

# Show the result
df_with_new_age.show()

