import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from pyspark.sql.types import IntegerType, StringType, StructField, StructType
from settings import LAYER

from utils.db_connections import mongo_connection
from utils.spark_builder import SparkBuilder
from utils.spark_writer import spark_writer

spark = SparkBuilder().s3_connector()

table = 'users'

data = mongo_connection(database='lake_solution', table=table)

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
])

dataframe = spark.createDataFrame(data, schema)

spark_writer(dataframe=dataframe, layer=LAYER, table=table)
