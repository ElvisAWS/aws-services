import json

def employee_test(event, context):
    body = "Hello from Lambda! employee Test"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }