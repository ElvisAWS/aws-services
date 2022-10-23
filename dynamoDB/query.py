import json  # module for converting Python objects to JSON
from decimal import Decimal
import boto3  # import Boto3
from boto3.dynamodb.conditions import Key


def queryEmployee(name, id):
    dynamodb = boto3.resource(
        'dynamodb')

    employee_table = dynamodb.Table('employees')
    # Loop through all the items and load each
    employee_list = employee_table.query(
        KeyConditionExpression=Key('name').eq(name)
        )
    for employee in employee_list['Items']:
        if employee['id'] == id:
            print("Employee is:", employee)


if __name__ == '__main__':
   queryEmployee("Loreal",1)