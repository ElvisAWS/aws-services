import boto3
from boto3.dynamodb.conditions import Key

def query_data_with_gsi():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('EmployeesGSI')
    
    response = table.query(
        IndexName='email',
        KeyConditionExpression=Key('email').eq('jdoe@test.com')
    )
    
    print(response['Items'][0])

query_data_with_gsi()