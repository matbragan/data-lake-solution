from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('sparkSession123').getOrCreate()

print(spark)
