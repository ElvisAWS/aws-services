import boto3
from boto3.dynamodb.conditions import Key

def query_data_with_lsi():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('EmployeesLSI')
    
    response = table.query(
        IndexName='user_name_subject',
        KeyConditionExpression=
            Key('user_name').eq('jon_doe') & Key('subject').eq('hiking')
    )
    
    print(response['Items'][0])

query_data_with_lsi()