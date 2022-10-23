
from botocore.exceptions import ClientError
import boto3
import json


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    id = event['id']
    name = event['name']
    dynamodb = boto3.resource(
        'dynamodb')
    # Specify the table to read from
    employees_table = dynamodb.Table('employees')

    try:
        response = employees_table.get_item(
            Key={'name': name,'id' : id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response['Item'])
        return response['Item']
