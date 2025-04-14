from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.getOrCreate()

data = [
    ("Alice", "HR", 5000),
    ("Bob", "HR", 4800),
    ("Charlie", "IT", 6000),
    ("David", "IT", 6200),
    ("Eve", "IT", 6100)
]
df = spark.createDataFrame(data, ["name", "department", "salary"])
df.show(truncate=False)
window_specif = Window.partitionBy("department").orderBy(df["salary"].desc())
df_with_row_num = df.withColumn("row_number",row_number().over(window_specif))
df_with_row_num.show(truncate=False)

df100 = df.groupby("department").sum("Salary")
df100.show(truncate=False)
# Use case ->

top_salary = df_with_row_num.filter("row_number = 1").drop("row_number")
top_salary.show(truncate=False)




