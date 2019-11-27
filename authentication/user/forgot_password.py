import json


def lambda_handler(event, context):
    """forgot password API"""
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email has been sent with password reset details",
        }),
    }
