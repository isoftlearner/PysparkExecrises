import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.getOrCreate()
# One way of writing "0.745"

df = spark.read.csv("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\imdb_top_1000.csv", header=True, inferSchema=True)
df.printSchema()
df.show(20)
#df = spark.read.format("csv").option("header",True).option("inferSchema",True).schema().load("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\imdb_top_1000.csv")

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
windowSpec = Window.partitionBy("Genre").orderBy("Released_Year")

#row_number()

df.withColumn("row_number",row_number().over(windowSpec)) \
.select("Series_Title","Released_Year","Genre","Runtime","row_number").show(10)

from pyspark.sql.functions import rank
df.withColumn("rank",rank().over(windowSpec)) \
.select("Series_Title","Released_Year","Genre","Runtime","rank").show(50)


from pyspark.sql.functions import dense_rank
df.withColumn("dense_rank",dense_rank().over(windowSpec)) \
.select("Series_Title","Released_Year","Genre","Runtime","dense_rank").show(50)

from pyspark.sql.functions import percent_rank
df.withColumn("percent_rank",percent_rank().over(windowSpec)) \
    .select("Series_Title","Released_Year","Genre","Runtime","percent_rank").show(10)

from pyspark.sql.functions import ntile
df.withColumn("ntile",ntile(2).over(windowSpec)) \
    .select("Series_Title","Released_Year","Genre","Runtime","ntile").show(10)

from pyspark.sql.functions import lag
df.withColumn("lag",lag("Runtime",1).over(windowSpec)) \
.select("Series_Title","Released_Year","Genre","Runtime","lag").show(10)

from pyspark.sql.functions import lead
df.withColumn("lead",lead("Runtime",1).over(windowSpec)) \
.select("Series_Title","Released_Year","Genre","Runtime","lead").show(10)


windowSpecAgg  = Window.partitionBy("Genre")
from pyspark.sql.functions import col,avg,sum,min,max,row_number
df.withColumn("row",row_number().over(windowSpec)) \
.withColumn("avg", avg(col("Runtime")).over(windowSpecAgg)) \
.withColumn("sum", sum(col("Runtime")).over(windowSpecAgg)) \
.withColumn("min", min(col("Runtime")).over(windowSpecAgg)) \
.withColumn("max", max(col("Runtime")).over(windowSpecAgg)) \
.where(col("row")==1).select("Genre","avg","sum","min","max") \
.show()