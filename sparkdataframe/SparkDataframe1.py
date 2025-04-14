from pyspark import SparkContext
sc = SparkContext("local","sample programe")
rdd1 = sc.parallelize([23,45,65,])
print(rdd1.collect())