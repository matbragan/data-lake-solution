from pipelines.utils.spark_builder import spark_builder

spark = spark_builder()

transactions = spark.read.parquet('s3a://lake-solution/transactions/')

transactions.show()
