#Question1 : Find the top 3 business purpose categories that generate the most miles driven for business purposes.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Initialize Spark session
spark = SparkSession.builder.appName("TopBusinessPurposes").getOrCreate()

# Sample data with integer and float values for miles
data = [
    ('2016-01-01 21:11', '2016-01-01 21:17', 'Business', 'Fort Pierce', 'Fort Pierce', 5.1, 'Meal/Entertain'),
    ('2016-01-02 01:25', '2016-01-02 01:37', 'Business', 'Fort Pierce', 'Fort Pierce', 5, None),
    ('2016-01-02 20:25', '2016-01-02 20:38', 'Business', 'Fort Pierce', 'Fort Pierce', 4.8, 'Errand/Supplies'),
    ('2016-01-05 17:31', '2016-01-05 17:45', 'Business', 'Fort Pierce', 'Fort Pierce', 4.7, 'Meeting'),
    ('2016-01-06 14:42', '2016-01-06 15:49', 'Business', 'Fort Pierce', 'West Palm Beach', 63.7, 'Customer Visit'),
    ('2016-01-06 17:15', '2016-01-06 17:19', 'Business', 'West Palm Beach', 'West Palm Beach', 4.3, 'Meal/Entertain'),
    ('2016-01-06 17:30', '2016-01-06 17:35', 'Business', 'West Palm Beach', 'Palm Beach', 7.1, 'Meeting')
]

# Define the schema explicitly
schema = StructType([
    StructField("start_date", StringType(), True),
    StructField("end_date", StringType(), True),
    StructField("category", StringType(), True),
    StructField("start", StringType(), True),
    StructField("stop", StringType(), True),
    StructField("miles", FloatType(), True),  # Ensure miles is of FloatType
    StructField("purpose", StringType(), True)
])

# Convert integer miles to float in the data manually or during DataFrame creation
data_with_float_miles = [(start_date, end_date, category, start, stop, float(miles), purpose)
                         for (start_date, end_date, category, start, stop, miles, purpose) in data]

# Create DataFrame with the explicit schema
df = spark.createDataFrame(data_with_float_miles, schema)
# Filter records where category is 'Business'
df_business = df.filter(col('category') == 'Business')
# Group by purpose and sum miles
result_df = df_business.groupBy('purpose').agg(sum_('miles').alias('total_miles'))

# Sort by total miles in descending order and take the top 3
result_df = result_df.orderBy(col('total_miles').desc()).limit(3)

# Show the result
result_df.show()