from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from utils.db_connections import mongo_connection
from utils.spark_builder import SparkBuilder

spark = SparkBuilder().s3_connector()

table = 'users'

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), True),
])

data = mongo_connection(database='lake_solution', table=table)

dataframe = spark.createDataFrame(data, schema)

dataframe.repartition(1)\
    .write.mode('overwrite')\
    .save(f's3a://lake-solution/extraction/{table}/')
