from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [("Apple", "Fruits", 1.5),
        ("Banana", "Fruits", 0.5),
        ("Carrot", "Vegetables", 0.8),
        ("Broccoli", "Vegetables", 1.2),
        ("Milk", "Dairy", 2.5),
        ("Cheese", "Dairy", 5.0)]

columns= ["product_name", "category", "price"]
df = spark.createDataFrame(data = data, schema = columns)

from pyspark.sql.window import Window

windowSpec = Window.partitionBy("category").orderBy("price".desc)