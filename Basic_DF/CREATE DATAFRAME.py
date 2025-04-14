from pyspark.sql import SparkSession
# Initialize Spark session
spark = SparkSession.builder.appName("TempViewExample").getOrCreate()
# Sample data (Name, Age, Department)
data = [("John", 25, "HR"),
        ("Sara", 30, "IT"),
        ("Mike", 35, "IT"),
        ("Anna", 28, "HR")]

# Column names
columns = ["Name", "Age", "Department"]
# Create DataFrame
df = spark.createDataFrame(data, columns)
# Show the DataFrame
df.show()
# Create a temporary view named "employee"
df.createOrReplaceTempView("employee")
# Now you can run SQL queries on this temporary view
result = spark.sql("SELECT * FROM employee WHERE Department = 'IT'")
result.show()
# Create a global temporary view named "employee_global"
df.createOrReplaceGlobalTempView("employee_global")
# Now you can run SQL queries on this global temporary view
result_global = spark.sql("SELECT * FROM global_temp.employee_global WHERE Age > 30")
result_global.show()

