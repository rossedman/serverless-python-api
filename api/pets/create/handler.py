from __future__ import print_function

import boto3
import json
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pets')

def handler(event, context):
    response = table.put_item(
       Item={
            'Id': int(event["id"]),
            'Name': event["name"],
            'Breed': event["breed"]
        }
    )

    return {}
