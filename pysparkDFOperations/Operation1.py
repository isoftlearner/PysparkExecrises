from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min

# Create a SparkSession
spark = SparkSession.builder.appName("SelectColumnsExample").getOrCreate()
# Assuming 'df' is a DataFrame
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
# Select specific columns using 'select'
df_select = df.select("Name")
#Selecting Columns with select and selectExpr:
# Select columns using SQL-like expressions with 'selectExpr'
df_select_expr = df.selectExpr("Name", "Age + 2 as Age_Plus_2")
df_select.show()

#Filtering Data with filter and where
df_filter = df.filter(df.Age > 30)
df_where = df.where(df.Age <= 30)
df_where.show(truncate=False)
df_filter.show(truncate=False)
#Grouping and Aggregating with groupBy and agg
df_group = df.groupBy("Age").agg(avg("Age").alias("Average_age"),max("Age").alias("Max_Age"),min("Age").alias("Min_Age"))
df_group.show()

#Sorting Data with orderBy and sort
# Sort data based on the 'Age' column in ascending order using 'orderBy'
df_asc = df.orderBy("Age")
# Sort data based on the 'Age' column in descending order using 'sort'
df_desc = df.sort(df.Age.desc())
