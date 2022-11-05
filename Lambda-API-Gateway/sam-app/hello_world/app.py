import json

import requests


def lambda_handler(event, context):
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    personId = event['queryStringParameters']['personId']
    return {
        "statusCode": 200,
        "body": json.dumps({
            "personId": personId + "From Lambda"
        }),
    }
