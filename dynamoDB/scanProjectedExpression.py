import boto3  # import Boto3


# You can use the ProjectionExpression parameter so that Scan only returns some of the attributes, rather than 
# all of them.

def scan_devices(display_employees_data, dynamodb=None, **kwargs):
    dynamodb = boto3.resource(
        'dynamodb')
    # Specify the table to scan
    devices_table = dynamodb.Table('employees')
    done = False
    start_key = None
    while not done:
        if start_key:
            kwargs['ExclusiveStartKey'] = start_key
        response = devices_table.scan(ProjectionExpression="info")
        display_employees_data(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    # A method for printing the items
    def print_employees(employees):
        for employee in employees:
            print(f"\n{employee['info']['address']} : {employee['info']['age']}")
            # print(employee)

    print(
        f"Scanning all employee data")
    # Print the items returned
    scan_devices(print_employees)