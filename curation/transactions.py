from utils.spark_builder import SparkBuilder

spark = SparkBuilder().s3_connector()

users = spark.read.load('s3a://lake-solution/extraction/users/')
sales = spark.read.load('s3a://lake-solution/extraction/sales/')

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
        sales.id.alias('sale_id'),
        sales.date.alias('sale_date'),
        sales.value.alias('sale_value')
    )
)

dataframe.repartition(1)\
    .write.mode('overwrite')\
    .save(f's3a://lake-solution/curation/transactions/')
