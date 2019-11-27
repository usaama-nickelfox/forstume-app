import json


def lambda_handler(event, context):
    """list of product API"""
    products = [{
        'title': '13 inch Sleeve/Slip Case',
        'colors': ['Grren', 'Grey', 'Yellow', 'Blue'],
        'price': 899,
        'images': ['http://amazon.com/13-inch-sleeve-slip/1.jpg', 'http://amazon.com/13-inch-sleeve-slip/2.jpg', 'http://amazon.com/13-inch-sleeve-slip/3.jpg'],
        'description': 'Cybertruck is built with an exterior shell made for ultimate durability and passenger protection. Starting with a nearly impenetrable exoskeleton, every component is designed for superior strength and endurance, from Ultra-Hard 30X Cold-Rolled stainless-steel structural skin to Tesla armor glass.'
    }, {
        'title': '13.3 inch Sleeve/Slip Case',
        'colors': ['Grren', 'Grey', 'Yellow', 'Blue'],
        'price': 1299,
        'images': ['http://amazon.com/13.3-inch-sleeve-slip/1.jpg', 'http://amazon.com/13.3-inch-sleeve-slip/2.jpg', 'http://amazon.com/13.3-inch-sleeve-slip/3.jpg'],
        'description': 'Cybertruck is built with an exterior shell made for ultimate durability and passenger protection. Starting with a nearly impenetrable exoskeleton, every component is designed for superior strength and endurance, from Ultra-Hard 30X Cold-Rolled stainless-steel structural skin to Tesla armor glass.'
    }, {
        'title': 'MOCA Handbag Sleeve carry case for 13.3 inch Old MacBook Air ',
        'colors': ['Grren', 'Grey', 'Yellow', 'Blue'],
        'price': 89,
        'images': ['http://amazon.com/13-inch-sleeve-slip/1.jpg', 'http://amazon.com/13-inch-sleeve-slip/2.jpg', 'http://amazon.com/13-inch-sleeve-slip/3.jpg'],
        'description': 'Cybertruck is built with an exterior shell made for ultimate durability and passenger protection. Starting with a nearly impenetrable exoskeleton, every component is designed for superior strength and endurance, from Ultra-Hard 30X Cold-Rolled stainless-steel structural skin to Tesla armor glass.'
    }
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(products),
    }
