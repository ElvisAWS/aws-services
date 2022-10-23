import json
from decimal import Decimal
import boto3  # import Boto3
from os.path import dirname, abspath
from os.path import dirname, abspath


def getAbsolutePath(filePath):
    path = dirname(dirname(abspath(__file__))) + filePath
    return path

def update_employees(name,id,age,address,genger,dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    # Specify the table
    devices_table = dynamodb.Table('employees')

    response = devices_table.update_item(
        Key={
            'device_id': name,
            'datacount': id
        },
        UpdateExpression="set info.age=:a,info.address=:d,info.genger=:g",
        ExpressionAttributeValues={
                ':a': age,
                ':d': address,
                ':g': genger
            
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
     with open(getAbsolutePath("/dynamoDB/data.json")) as json_file:
        employee_list = json.load(json_file, parse_float=Decimal)
     update_response = update_employees("Darius",3,30,"three street","Female")
     print(update_response)