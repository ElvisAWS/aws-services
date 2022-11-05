import json

def employee_prod(event, context):
    body = "Hello from Lambda! employee Prod"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }