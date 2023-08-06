import io
import os

import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from dotenv import load_dotenv

load_dotenv()

aws_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')


def write_s3(
    data: list,
    file_name: str,
    bucket_name: str = 'hotmart-case'
) -> None:

    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)

    buffer = io.BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_key,
        aws_secret_access_key=aws_secret_key
    )

    file_name = f'{file_name}.parquet'

    s3.upload_fileobj(buffer, bucket_name, file_name)
