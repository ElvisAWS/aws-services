import boto3  # import Boto3


# scans the employees table with no filter_expression.

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
        response = devices_table.scan()
        display_employees_data(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    # A method for printing the items
    def print_employees(employees):
        for employee in employees:
            print(f"\n{employee['name']} : {employee['id']}")
            print(employee['info'])

    print(
        f"Scanning all employee data")
    # Print the items returned
    scan_devices(print_employees)