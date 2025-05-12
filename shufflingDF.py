from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Shuffle Example").getOrCreate()

# Create a DataFrame with some data
data = [
    (1, "Ahmed", 100, "2022-01-01"),
    (2, "John", 200, "2022-01-02"),
    (3, "Fabrice", 300, "2022-01-03"),
    (4, "Mehdi", 400, "2022-01-04"),
    (5, "Mehdi", 500, "2022-01-05")
]

columns = ["id", "customer", "amount", "order_date"]

df = spark.createDataFrame(data, columns)
print("before")
# Group the data by the "customer" column and sum the amount
groupedData = df.groupBy("customer").sum("amount")

# Show the result
groupedData.show()
