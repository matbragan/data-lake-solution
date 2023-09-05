import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from utils.db_connections import mongo_connection
from utils.spark_builder import SparkBuilder
from utils.spark_writer import SparkWriter

builder = SparkBuilder()
spark = builder()

table = 'users'

data = mongo_connection(database='lake_solution', table=table)

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
])

dataframe = spark.createDataFrame(data, schema)

writer = SparkWriter(spark=spark, path='batch_extraction/users/')
writer.s3_writer(dataframe=dataframe)
writer.vacuum_and_optimize()
