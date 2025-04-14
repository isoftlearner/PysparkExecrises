from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank

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
df.show(truncate=False)
#rank employees within each department, by salary (highest first):
windowSpec = Window.partitionBy("department").orderBy(df["salary"].desc())
df_with_rank = df.withColumn("rank",rank().over(windowSpec))
df_with_rank.show()
df_with_rank = df.withColumn("rank", dense_rank().over(windowSpec))
df_with_rank.show()
