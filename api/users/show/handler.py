from __future__ import print_function

import boto3
import json
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def handler(event, context):

    response = table.get_item(
        Key={
            'uuid': str(event["body"]["uuid"])
        }
    )

    return response["Item"]