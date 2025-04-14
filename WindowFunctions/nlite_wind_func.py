from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import ntile

spark = SparkSession.builder.appName("NtileExample").getOrCreate()

data = [("Alice", 90), ("Bob", 85), ("Carol", 80), ("Dave", 75),
        ("Emma", 70), ("Frank", 65), ("Grace", 60), ("Helen", 55),("Helen", 55)]

df = spark.createDataFrame(data, ["student", "score"])
df.show(truncate=False)
# Define the window
windowSpec = Window.orderBy("score")

# Apply NTILE to split into 4 parts
df.withColumn("quartile", ntile(2).over(windowSpec)).show()
