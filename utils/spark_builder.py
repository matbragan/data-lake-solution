import os

from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()


class SparkBuilder():

    def __init__(self):
        self.aws_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_credentials_provider = 'SimpleAWSCredentialsProvider'

        self.builder = SparkSession.builder.appName('data-lake-solution')

    def s3_connector(self):
        self.builder = (
            self.builder
            .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.2')
            .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.aws.credentials.provider', f'org.apache.hadoop.fs.s3a.{self.aws_credentials_provider}')
            .config('spark.hadoop.fs.s3a.access.key', self.aws_key)
            .config('spark.hadoop.fs.s3a.secret.key', self.aws_secret_key)
        )

        spark = self.builder.getOrCreate()

        return spark
