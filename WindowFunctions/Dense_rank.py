from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank

spark = SparkSession.builder.getOrCreate()

data = [
    ("Alice", "HR", 5000),
    ("Bob", "HR", 4800),
    ("Clara", "HR", 5000),
    ("David", "IT", 6200),
    ("Eve", "IT", 6100),
    ("Frank", "IT", 6100)
]

df = spark.createDataFrame(data, ["name", "department", "salary"])

windowSpec = Window.partitionBy("department").orderBy(df["salary"].desc())
df_with_dense_rank = df.withColumn("dense_rank", dense_rank().over(windowSpec))
df_with_dense_rank.show()
