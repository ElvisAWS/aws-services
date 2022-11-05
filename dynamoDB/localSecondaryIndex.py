

# Some applications only need to query data using the base table’s primary key. However, there might be situations 
# where an alternative sort key would be helpful. To give your application a choice of sort keys, you can create
# one or more local secondary indexes on an Amazon DynamoDB table and issue Query or Scan requests against these 
# indexes.


import boto3
from boto3.dynamodb.conditions import Key

def create_table_with_lsi():
    dynamodb = boto3.resource('dynamodb')
    table_name= 'EmployeesLSI'
    
    table = dynamodb.create_table(
        TableName= table_name,
        KeySchema=[
            {
                'AttributeName': 'user_name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'user_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'subject',
                'AttributeType': 'S'
            },
    
        ],
        LocalSecondaryIndexes=[
            {
                'IndexName': 'user_name_subject',
                'KeySchema': [
                    {
                        'AttributeName': 'user_name',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'subject',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
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

def create_posts():
    post1 = {
        'title': "My favorite hiking spots",
        'user_name': 'jon_doe',
        'subject': 'hiking'
    }
    post2 = {
        'title': "My favorite recipes",
        'user_name': 'jon_doe',
        'subject': 'cooking'
    }
    post3 = {
        'title': "I love hiking!",
        'user_name': 'jane_doe',
        'subject': 'hiking'
    }
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EmployeesLSI')
    table.put_item(Item=post1)
    table.put_item(Item=post2)
    table.put_item(Item=post3)

if __name__ == '__main__':
    dax_table = create_table_with_lsi()
    print(f"Created table.")
    create_posts()
    print(f"updating table.")