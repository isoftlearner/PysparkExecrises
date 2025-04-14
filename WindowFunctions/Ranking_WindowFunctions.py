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
df = spark.createDataFrame(data, ["Name", "Department", "Salary"])
# Define a window
window = Window.partitionBy("Name").orderBy("Salary")
# Apply ranking window functions
df.withColumn("Row Number", F.row_number().over(window)) \
  .withColumn("Rank", F.rank().over(window)) \
  .withColumn("Dense Rank", F.dense_rank().over(window)) \
  .withColumn("Percent Rank", F.percent_rank().over(window)) \
  .show()