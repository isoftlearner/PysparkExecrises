import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.getOrCreate()
# One way of writing
salesByMake = spark.read.format('csv') \
                        .option("inferSchema", True) \
                        .option("header", True) \
                        .option("sep", ',') \
                .load('E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\norway_new_car_sales_by_make.csv')
salesByModel = spark.read.csv('E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\norway_new_car_sales_by_make.csv', header = True, inferSchema = True)
#Displaying the data frame:
salesByMake.show(4)

#Printing the Schema of a data frame:
salesByMake.printSchema()

#Retrieving the columns in a list:
print(salesByMake.columns)

#Counting the rows in a data frame:
print(salesByMake.count())

#Select required columns (.select()): Since data frames are immutable, you will either have to store them in a different variable name or in the same name.
df = salesByModel.select('Year', 'Month', 'Make', 'Quantity')
df.show(10)
#Change the name of existing columns(.withColumnRenamed())
from pyspark.sql.functions import *
salesByModel.withColumnRenamed('Year', 'YEAR') \
            .withColumnRenamed('Month', 'MONTH') \
            .withColumnRenamed('Make', 'MAKE')
# Using alias is faster than using withColumnRenamed() function. So avoid to many withColumnRenamed
salesByModel.select(col('Year').alias('YEAR'), col('Month').alias('MONTH'))

'''
if(col('QUANTITy)>=1000:
       PRINT("HIGH)
else:
  if(col('QUANTITY)>=500: and col('QUATITY')<1000):
       Print("medium")
  else
   print("low)
'''

#Add a new column to the data frame: Using when().otherwise() for giving conditions. You can think of it as an if-else block.
condition = when(col('Quantity')>=1000, "High").otherwise(when((col('Quantity')>=500) & (col('Quantity')<1000), "Medium").otherwise("Low"))
df.withColumn('Range>1000', col('Quantity')>1000).withColumn('RangeVal', condition).show()


#df.filter():filters as per the specified condition
df.filter(trim(col('Make')) == 'Volkswagen').show(2)

#groupBy & orderBy: you should groupBy all the items and then apply aggregation functions such as min, max, sum, avg, count etc.
#Note: orderBy and Sort do the same thing.

salesByModel.groupBy('Make').agg(sum('Quantity').alias('SumQuantity'), avg('Pct').alias('AvgPct')).orderBy('SumQuantity').show()

#Joins: In place of how you can give inner, left, right, left_outer, etc..The “inner” join is the default when no other join is specified.

# Syntax:
# df1.join(df2, oncondition, how = "inner")
salesByModel.join(salesByMake, trim(salesByMake["Make"]) == trim(salesByModel["Make"])).show()


salesByModel.join(salesByMake,
                  trim(salesByMake["Make"]) == trim(salesByModel["Make"]),
                  how = "inner") \
            .select(salesByMake["Year"],
                    salesByMake.Month,
                    salesByModel["Pct"],
                    salesByModel.Make) \
            .show(5)

#SQL Window Function:
from pyspark.sql.window import Window
Parition_Param = Window().partitionBy(col('Make')).orderBy('Pct')
salesByModel.withColumn('Sum',sum('Quantity').over(Parition_Param)).show(4)

#df.repartition(1).write.mode('overwrite').format("csv").save("location")
# or
#df.coalesce(1).write.mode('overwrite').format("csv").save("E:\\ONLINE_CLASS_TECH_V1\\pysparkTestfiles\\sample3\\output\\")'''
