import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from pyspark.sql.types import (DateType, FloatType, IntegerType, StructField,
                               StructType)
from settings import LAYER

from utils.db_connections import mysql_connection
from utils.spark_builder import SparkBuilder
from utils.spark_writer import spark_writer

spark = SparkBuilder().s3_connector()

table = 'sales'

data = mysql_connection(database='lake_solution', table=table)

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('user_id', IntegerType(), False),
    StructField('date', DateType(), True),
    StructField('value', FloatType(), True),
])

dataframe = spark.createDataFrame(data, schema)

spark_writer(dataframe=dataframe, layer=LAYER, table=table)
