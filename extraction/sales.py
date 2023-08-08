from pyspark.sql.types import (DateType, FloatType, IntegerType, StructField,
                               StructType)

from utils.db_connections import mysql_connection
from utils.spark_builder import spark_builder

spark = spark_builder()

table = 'sales'

schema = StructType([
    StructField('id', IntegerType(), False),
    StructField('user_id', IntegerType(), False),
    StructField('date', DateType(), True),
    StructField('value', FloatType(), True),
])

data = mysql_connection(database='lake_solution', table=table)

dataframe = spark.createDataFrame(data, schema)

dataframe.repartition(1)\
    .write.mode('overwrite')\
    .save(f's3a://lake-solution/extraction/{table}/')
