import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from pyspark.sql.types import (DateType, FloatType, IntegerType, StructField,
                               StructType)

from utils.db_connections import mysql_connection
from utils.spark_builder import SparkBuilder
from utils.spark_writer import SparkWriter

builder = SparkBuilder()
spark = builder()

table = 'sales'

data = mysql_connection(database='lake_solution', table=table)

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('user_id', IntegerType(), False),
    StructField('date', DateType(), True),
    StructField('value', FloatType(), True),
])

dataframe = spark.createDataFrame(data, schema)

writer = SparkWriter(spark=spark, path='batch_extraction/sales/')
writer.s3_writer(dataframe=dataframe)
writer.vacuum_and_optimize()
