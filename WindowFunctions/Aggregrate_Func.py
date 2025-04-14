from pyspark.sql import SparkSession
from pyspark.sql import functions
from pyspark.sql import Window
# Create a SparkSession
spark = SparkSession.builder.appName("Window Functions").getOrCreate()
# Create a sample DataFrame
data = [
    ("John", "Sales", 1000),
    ("John", "Sales", 2000),
    ("John", "Marketing", 3000),
    ("Jane", "Sales", 4000),
    ("Jane", "Marketing", 5000)
]
df = spark.createDataFrame(data, ["Name", "Department", "Salary"])
# Define a window
window = Window.partitionBy("Name")
# Apply aggregate window functions
df.withColumn("Total Salary", functions.sum("Salary").over(window)) \
  .withColumn("Average Salary", functions.avg("Salary").over(window)) \
  .withColumn("Max Salary", functions.max("Salary").over(window)) \
  .withColumn("Min Salary", functions.min("Salary").over(window)) \
  .withColumn("Count", functions.count("Salary").over(window)) \
  .show()