from pipelines.utils.spark_builder import spark_builder

spark = spark_builder()

users = spark.read.parquet('s3a://lake-solution/users.parquet')
sales = spark.read.parquet('s3a://lake-solution/sales.parquet')

sales = (
    sales
    .withColumnsRenamed({
        '0': 'id',
        '1': 'user_id',
        '2': 'date',
        '3': 'value'
    })
)

output = (
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

output.write.save('s3a://lake-solution/transactions/')
