from pyspark.sql import SparkSession
from pyspark.sql.functions import col
# Initialize Spark session
spark = SparkSession.builder.master("local").appName("Type Casting Example").getOrCreate()
# Sample data with mixed data types
data = [
    (1, "100"),  # First value is an integer, second is a string
    (2, "200"),
    (3, "300")
]
# Create a DataFrame
df = spark.createDataFrame(data, ["id", "amount"])
# Show the original DataFrame
df.show()
# Type casting: Convert 'amount' column (which is a string) to integer
df_casted = df.withColumn("amount", col("amount").cast("int"))
# Show the DataFrame after type casting
df_casted.show()
# Type casting: Convert 'id' column (which is an integer) to string
df_casted_to_string = df_casted.withColumn("id", col("id").cast("string"))

# Show the DataFrame after converting 'id' to string
df_casted_to_string.show()
