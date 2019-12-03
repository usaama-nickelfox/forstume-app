import os

import boto3
import pytest
import yaml

from authentication.user.login import lambda_handler, str_compare

with open(os.path.join(os.path.dirname(__file__), 'dataset.yaml'), 'r') as stream:
    try:
        feature_dataset = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


class TestLogin(object):
    test_data = feature_dataset.get('Authentication')

    @pytest.mark.parametrize("event", test_data.get('LoginFeature'))
    def test_login_check(self, event):
        expected = event.pop('expected')
        response = lambda_handler(event=event, context={})
        assert response['statusCode'] == expected

    @pytest.mark.parametrize("data", test_data.get('StrCompareFeature'))
    def test_str_compare(self, data):
        expected = data.pop('expected')
        response = str_compare(**data)
        assert response == expected

    def test_dynamo_products(self):
        """Test dynamo products records"""
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('products')
        item = table.get_item(Key={
            'id': '68928f52-15c7-11ea-99c0-f35332b3c31a',
            'type': 'mobile'
        })['Item']
        assert item['name'] == 'samsung'
