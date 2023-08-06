import os

from dotenv import load_dotenv
from pyspark import SparkConf
from pyspark.sql import SparkSession

load_dotenv()


def spark_builder() -> SparkSession:
    aws_key = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_credentials_provider = 'SimpleAWSCredentialsProvider'

    conf = SparkConf()
    conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.2')

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    spark.conf.set(
        'spark.hadoop.fs.s3a.impl',
        'org.apache.hadoop.fs.s3a.S3AFileSystem'
    )
    spark.conf.set(
        'spark.hadoop.fs.s3a.aws.credentials.provider',
        f'org.apache.hadoop.fs.s3a.{aws_credentials_provider}'
    )
    spark.conf.set('spark.hadoop.fs.s3a.access.key', aws_key)
    spark.conf.set('spark.hadoop.fs.s3a.secret.key', aws_secret_key)

    return spark
