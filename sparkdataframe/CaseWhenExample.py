from pyspark.sql import SparkSession
# Start Spark session
spark = SparkSession.builder.appName("CaseWhenExample").getOrCreate()
# Sample Data
data = [("Alice", 25),
        ("Bob", 30),
        ("Carol", 18),
        ("David", 65)]
# Define Schema
columns = ["Name", "Age"]
# Create DataFrame
df = spark.createDataFrame(data, columns)

# Apply CASE WHEN using SQL Expression
df_new = df.selectExpr(
    "*",  # Select all existing columns
    "CASE WHEN Age < 20 THEN 'Teen' " +
         "WHEN Age BETWEEN 20 AND 50 THEN 'Adult' " +
         "ELSE 'Senior' END as Age_Category"
)
df_new.show()
