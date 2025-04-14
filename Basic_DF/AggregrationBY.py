from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("GroupByExample").getOrCreate()
data = [("John", "HR", 3000),
        ("Sara", "IT", 4500),
        ("Mike", "IT", 5000),
        ("Anna", "HR", 3500)]

columns = ["Name", "Department", "Salary"]
df = spark.createDataFrame(data, columns)
df.show()
from pyspark.sql import functions as F
# Group by "Department" and calculate the average salary
df_grouped = df.groupBy("Department").agg(F.avg("Salary").alias("AvgSalary"))

df_grouped.show()
