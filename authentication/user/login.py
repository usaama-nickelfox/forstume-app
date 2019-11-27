import json


def lambda_handler(event, context):
    """Login API"""
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User successfully Logged in",
        }),
    }
