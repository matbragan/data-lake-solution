import os

from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()

aws_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

spark = SparkSession.builder.appName('read-s3').getOrCreate()

spark.conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
spark.conf.set('spark.hadoop.fs.s3a.access.key', aws_key)
spark.conf.set('spark.hadoop.fs.s3a.secret.key', aws_secret_key)

df = spark.read.parquet('s3a://hotmart-case/users.parquet')

df.show()
