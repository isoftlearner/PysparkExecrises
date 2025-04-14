from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName('SelectColumnsExample').getOrCreate()
# Sample data (Name, Age, Salary)
data = [("John", 25, 3000), ("Sara", 30, 4500), ("Mike", 35, 5000)]

# Define column names
columns = ["Name", "Age", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()
# Select only the "Name" and "Age" columns
df_selected = df.select("Name", "Age")

# Show the selected columns
df_selected.show()
from pyspark.sql.functions import col

# Select columns and create a new column "SalaryInThousands"
df_selected = df.select("Name", "Age", (col("Salary") / 1000).alias("SalaryInThousands"))

# Show the result
df_selected.show()
