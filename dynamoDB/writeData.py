import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
import boto3  # import Boto3
from os.path import dirname, abspath


def getAbsolutePath(filePath):
    path = dirname(dirname(abspath(__file__))) + filePath
    return path


def write_data(employee_list):
    dynamodb = boto3.resource(
        'dynamodb')

    employee_table = dynamodb.Table('employees')
    # Loop through all the items and load each
    for employee in employee_list:
        employee_name = (employee['name'])
        employee_id = employee['id']
        # Print device info
        print("Loading Devices Data:", employee_name, employee_id)
        employee_table.put_item(Item=employee)


if __name__ == '__main__':
    # open file and read all the data in it
    with open(getAbsolutePath("/dynamoDB/data.json")) as json_file:
        employee_list = json.load(json_file, parse_float=Decimal)
    write_data(employee_list)