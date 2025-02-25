import logging
from botocore.exceptions import ClientError
import boto3
from botocore.config import Config
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

CONFIG = Config(
    region_name=os.environ.get('AWS_DEFAULT_REGION'),

)
s3_client = boto3.client('s3', config=CONFIG)
BUCKET = os.environ.get('AWS_S3_BUCKET_NAME')


def download_file(file_name, aws_path):
    path = Path(f'uploads').resolve()
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / file_name
    s3_client.download_file(BUCKET, aws_path, file_path)
    return file_path
