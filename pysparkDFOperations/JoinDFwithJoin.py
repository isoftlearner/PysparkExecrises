from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("JoinedDF").getOrCreate()
#Joining DataFrames with join
# Assuming 'df_1' and 'df_2' are DataFrames with columns 'ID' and 'Salary'
df_1 = spark.createDataFrame([(1, 1000), (2, 2000)], ["ID", "Salary"])
df_2 = spark.createDataFrame([(1, 500), (3, 300)], ["ID", "Salary"])
df_join = df_1.join(df_2,on="ID")
df_join.show()
#Combining Data with union
df_unioin = df_1.union(df_2)
df_unioin.show(truncate=False)
#Adding and Renaming Columns with withColumn and withColumnRenamed
# Add a new column 'City' with a constant value
df_with_column = df_1.withColumn("City", "New York")
df_with_column.show(truncate=False)
# Rename the 'Name' column to 'FullName'
df_with_column_renamed = df_1.withColumnRenamed("ID", "IDENTIFICATION")
df_with_column.show()

# Assuming 'df' is a DataFrame
data = [("Alice", 30), ("Bob", 35), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
#Removing Columns and Duplicates with drop and dropDuplicates
# Drop the 'Age' column
df_drop_column = df.drop("Age")
# Remove duplicate rows based on all columns
df_no_duplicates = df.dropDuplicates()
df_drop_column.show()
df_no_duplicates.show()
#Getting Distinct Rows with distinct
df_distinct = df.distinct()
df_distinct.show()