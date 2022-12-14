
# Craete dynamoDB Table


# Craete dynamoDB Table

import boto3


def create_dax_table(dyn_resource=None):
    """
    Creates a DynamoDB table.

    :param dyn_resource: Either a Boto3 or DAX resource.
    :return: The newly created table.
    """
    if dyn_resource is None:
        dyn_resource = boto3.resource('dynamodb')

    table_name = 'employees'
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'id', 'KeyType': 'HASH'}, # partition_key
            {'AttributeName': 'name', 'KeyType': 'RANGE'} # sort_key
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'name', 'AttributeType': 'S'},
            {'AttributeName': 'id', 'AttributeType': 'N'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    }
    table = dyn_resource.create_table(**params)
    print(f"Creating {table_name}...")
    table.wait_until_exists()
    return table


if __name__ == '__main__':
    dax_table = create_dax_table()
    print(f"Created table.")