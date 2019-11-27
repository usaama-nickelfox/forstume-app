import json


def lambda_handler(event, context):
    """Sign up API"""
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User successfully registered.",
        }),
    }
