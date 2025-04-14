from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Class3').getOrCreate()
data = [("James", "Sales", 3000), \
    ("Michael", "Sales", 4600), \
    ("Robert", "Sales", 4100), \
    ("Maria", "Finance", 3000), \
    ("James", "Sales", 3000), \
    ("Scott", "Finance", 3300), \
    ("Jen", "Finance", 3900), \
    ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000), \
    ("Michael", "Sales", 4100) \
  ]

columns= ["employee_name", "department", "salary"]
df1 = spark.createDataFrame(data=data,schema=columns)
df1.printSchema()
df1.show(truncate=False)
distinctDF = df1.distinct()
print("Distinct count: "+str(distinctDF.count()))
distinctDF.show(truncate=False)

df2 = df1.dropDuplicates()
print("Distinct count: "+str(df2.count()))
df2.show(truncate=False)

dropDisDF = df1.dropDuplicates(["department","salary"])
print("Distinct count of department salary : "+str(dropDisDF.count()))
dropDisDF.show(truncate=False)


