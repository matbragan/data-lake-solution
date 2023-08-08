from utils.spark_builder import spark_builder

spark = spark_builder()

users = spark.read.load('s3a://lake-solution/extraction/users/')
sales = spark.read.load('s3a://lake-solution/extraction/sales/')
transactions = spark.read.load('s3a://lake-solution/curation/transactions/')

users.show()
sales.show()
transactions.show()
