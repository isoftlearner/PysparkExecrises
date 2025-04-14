from pyspark.sql import SparkSession
from pyspark.sql import functions as F
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
# Define a window
window = Window.partitionBy("Name").orderBy("Salary")
df = spark.createDataFrame(data, ["Name", "Department", "Salary"])
# Apply analytical window functions
df.withColumn("Previous Salary", F.lag("Salary").over(window)) \
  .withColumn("Next Salary", F.lead("Salary").over(window)) \
  .withColumn("First Salary", F.first("Salary").over(window)) \
  .withColumn("Last Salary", F.last("Salary").over(window)) \
  .show()