import json


def lambda_handler(event, context):
    """list of product API"""
    blogs = [
        'Personal',
        'Corporate',
        'Artist',
        'Sports',
        'Podcast'
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(blogs),
    }
