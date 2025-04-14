from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import lag, desc, lead

spark = SparkSession.builder.getOrCreate()
data = [
    ("vijay", "2023-01", 4500),
    ("vijay", "2023-02", 4700),
    ("vijay", "2023-03", 4900),
    ("kumar", "2023-01", 4000),
    ("kumar", "2023-02", 4100),
    ("ravi", "2023-02", 5100),
   ("ravi", "2023-01", 2500),
   ("ravi", "2023-03", 4100),

]
df = spark.createDataFrame(data, ["name", "month", "salary"])
df.show(truncate=False)
windowspec = Window.partitionBy("name").orderBy(desc("month"))
df_with_lag = df.withColumn("Current_salary",lag('salary',1).over(windowspec))
df_with_lag.show(truncate=False)
df_with_lead = df.withColumn("next_salary", lead("salary", 1).over(windowSpec))
df_with_lead.show()
#from pyspark.sql.functions import col
#df_with_Comparing = df_with_lag.withColumn("ComparingSalay",col("Current_salary") - col("salary"))
#df_with_Comparing.show(truncate=False)
from pyspark.sql.functions import col
#Use case:- Calculate salary change
from pyspark.sql.functions import expr
#df_with_change = df_with_lag.withColumn("salary_change", col("salary") - col("prev_salary"))
#df_with_change.show()