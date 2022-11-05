import json

def employee_test(event, context):
    request_body = {
        'Hello from Lambda! employee Test',
         context.function_version,
         context.aws_request_id,
         context.invoked_function_arn
    }
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(list(request_body)),
        "headers": {
            "Content-Type": "application/json"
        }
    }