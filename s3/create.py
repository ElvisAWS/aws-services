import logging
import boto3
from botocore.exceptions import ClientError
logger = logging.getLogger(__name__)

def create_bucket(bucket_name):
    s3_client = boto3.client('s3',region_name='eu-west-2')
    # Create bucket
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
    'LocationConstraint': 'eu-west-2'})
        print("Created bucket %s with ARN %s.", bucket_name)
        logger.info("Created bucket %s with ARN %s.", bucket_name)
    except ClientError as e:
        logger.exception(e,"Couldn't create bucket %s.", bucket_name)
    return False

create_bucket('my-s3-sns-demo1-bucket')