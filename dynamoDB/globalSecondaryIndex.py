
# Some applications might need to perform many kinds of queries, using a variety of different attributes as 
# query criteria. To support these requirements, you can create one or more global secondary indexes and issue 
# Query requests against these indexes in Amazon DynamoDB.
# To illustrate this we’re going to create an Employee table with employee_id as our hash kay and email address 
# as our GSI.

import boto3
from boto3.dynamodb.conditions import Key

def create_table_with_gsi():
    dynamodb = boto3.resource('dynamodb')
    table_name = 'EmployeesGSI'
    
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'emp_id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'emp_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },
    
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'email',
                'KeySchema': [
                    {
                        'AttributeName': 'email',
                        'KeyType': 'HASH'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput' :{
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1,
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    print("Table status:", table.table_status)
    print(f"Creating {table_name}...")
    table.wait_until_exists()
    return table
    
def create_employee():
    user = {
        'emp_id': 1,
        'first_name': 'Jon',
        'last_name': 'Doe',
        'email': 'jdoe@test.com'
    }
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EmployeesGSI')
    table.put_item(Item=user)

if __name__ == '__main__':
    dax_table = create_table_with_gsi()
    print(f"Created table.")
    create_employee()
    print(f"updating table.")