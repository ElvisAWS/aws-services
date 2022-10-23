# import Boto3 exceptions and error handling module
# To use the get_item function, we need to pass both keys to the get_item api
from botocore.exceptions import ClientError
import boto3  # import Boto3


def get_Employees(name,id, dynamodb=None):
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
        return response['Item']


if __name__ == '__main__':
    employees = get_Employees('Loreal',1)
    if employees:
        print("Get employees Data Done:")
        # Print the data read
        print(employees)