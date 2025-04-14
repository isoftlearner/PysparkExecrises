from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Spark Class1').getOrCreate()
str = "Hello world"
# spark session created
print(spark)

#How to create spark create datafrmae

"""
    def createDataFrame(  # type: ignore[misc]
        self,
        data: Union[RDD[Any], Iterable[Any], "PandasDataFrameLike", "ArrayLike"],
        schema: Optional[Union[AtomicType, StructType, str]] = None,
        samplingRatio: Optional[float] = None,
        verifySchema: bool = True,
    ) -> DataFrame:
"""
data = [("James,,Smith",["Java","Scala","C++"],"CA"), \
    ("Michael,Rose,",["Spark","Java","C++"],"NJ"), \
    ("Robert,,Williams",["CSharp","VB"],"NV")]
columns = ["name","languagesAtSchool","currentState"]
df = spark.createDataFrame(data,schema=columns)
df.show()

str = "Hello , world"
print(str.split(","))




