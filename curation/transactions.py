import sys

sys.path.insert(1, '/home/matbragan/Documents/data-lake-solution/')

from settings import LAYER

from utils.spark_builder import SparkBuilder
from utils.spark_writer import spark_writer

spark = SparkBuilder().s3_connector()

users = spark.read.load('s3a://lake-solution/raw/users/')
sales = spark.read.load('s3a://lake-solution/raw/sales/')

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

spark_writer(dataframe=dataframe, layer=LAYER, table='transactions')
