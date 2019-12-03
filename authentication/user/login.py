import json


def str_compare(str1, str2):
    if str1 == str2:
        return True
    else:
        return False


def lambda_handler(event, context):
    """Login API"""
    if event['email'] == 'info@forstume-app.com' and event['password'] == 'password':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "User successfully Logged in",
            }),
        }
    else:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "message": "Failed to login",
            }),
        }
