import boto3
import logging
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)
# Delete all existing buckets

def delete_bucket(bucket_name):
    try:
        client = boto3.client("s3")
        client.delete_bucket(Bucket=bucket_name)
        print(f"Amazon S3 Bucket has been deleted: {bucket_name}")
    except ClientError as e:
        logger.exception(e)

delete_bucket('my-s3-sns-demo1-bucket')
