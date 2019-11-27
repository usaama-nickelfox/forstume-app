import json


def lambda_handler(event, context):
    """list of product API"""
    blogs = [{
        'title': 'BETTER UTILITY THAN A TRUCK WITH MORE PERFORMANCE THAN A SPORTS CAR',
        'description': 'Cybertruck is built with an exterior shell made for ultimate durability and passenger protection. Starting with a nearly impenetrable exoskeleton, every component is designed for superior strength and endurance, from Ultra-Hard 30X Cold-Rolled stainless-steel structural skin to Tesla armor glass.'
    }, {
        'title': 'ULTRA-HARD 30X COLD-ROLLED STAINLESS STEEL',
        'description': 'If there was something better, we’d use it. Help eliminate dents, damage and long-term corrosion with a smooth monochrome exoskeleton that puts the shell on the outside of the car and provides you and your passengers maximum protection.'
    }, {
        'title': 'TESLA ARMOR GLASS',
        'description': 'Ultra-strong glass and polymer-layered composite can absorb and redirect impact force for improved performance and damage tolerance.'
    }
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(blogs),
    }
