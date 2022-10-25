import json

import requests


def get_employee(event, context):
    personId = event['queryStringParameters']['personId']
    
    if personId == '1':
        return {
        "statusCode": 200,
        "body": json.dumps({
            "personId": personId + " :Employee name is Jon"
        }),
    }
    else:
        return {
        "statusCode": 200,
        "body": json.dumps({
            "personId": personId + " :Employee does not exist"
        }),
    }

def create_employee(event, context):
    payLoad = event['body']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "Employee":payLoad
        }),
    }

def delete_employee(event, context):
    personId = event['queryStringParameters']['personId']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "Employee":"Successfully deleted Employee with id: " + personId
        }),
    }

def update_employee(event, context):
    personId = event['queryStringParameters']['personId']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "Employee":"Successfully updated Employee with id: " + personId
        }),
    }
