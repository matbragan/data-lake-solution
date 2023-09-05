import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from utils.spark_builder import SparkBuilder
from utils.spark_writer import SparkWriter

builder = SparkBuilder()
spark = builder()

users = spark.read.load('s3a://lake-solution/batch_extraction/users/')
sales = spark.read.load('s3a://lake-solution/batch_extraction/sales/')

dataframe = (
    users
    .join(
        sales,
        users.id == sales.user_id,
        'left'
    )
    .select(
        users.id.alias('user_id'),
        users.name.alias('user_name'),
        sales.id.alias('transaction_id'),
        sales.date.alias('transaction_date'),
        sales.value.alias('transaction_value')
    )
)

writer = SparkWriter(spark=spark, path='batch_curated/transactions/')
writer.s3_writer(dataframe=dataframe)
writer.vacuum_and_optimize()
