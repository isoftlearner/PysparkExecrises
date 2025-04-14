from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import lead, desc

spark = SparkSession.builder.getOrCreate()
data = [
    ("Alice", "2023-01", 4500),
    ("Alice", "2023-02", 4700),
    ("Alice", "2023-03", 4900),
    ("Bob", "2023-01", 4000),
    ("Bob", "2023-02", 4100),
]
df = spark.createDataFrame(data, ["name", "month", "salary"])
from pyspark.sql.window import Window
windowSpec = Window.partitionBy("name").orderBy(desc("month"))
#use case:- Use lead() to see each person’s next month’s salary:
df_with_lead = df.withColumn("next_salary", lead("salary", 1).over(windowSpec))
df_with_lead.show()
