import os

from dotenv import load_dotenv
from pyspark.sql import SparkSession

load_dotenv()


class SparkBuilder():

    def __init__(self):
        self.builder = SparkSession.builder.appName('data-lake-solution') \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.2,io.delta:delta-core_2.12:1.0.0')

    def __call__(self):
        self.s3_connector()
        # self.delta_connector()
        
        return self.builder.getOrCreate()

    def s3_connector(self):
        aws_key = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        aws_credentials_provider = 'SimpleAWSCredentialsProvider'
        
        self.builder = (
            self.builder
            .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.aws.credentials.provider', f'org.apache.hadoop.fs.s3a.{aws_credentials_provider}')
            .config('spark.hadoop.fs.s3a.access.key', aws_key)
            .config('spark.hadoop.fs.s3a.secret.key', aws_secret_key)
        )

    def delta_connector(self):
        self.builder = (
            self.builder
            .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension')
            .config('spark.sql.catalog.spark_catalog', 'org.apache.spark.sql.delta.catalog.DeltaCatalog')
        )
