from __future__ import print_function

import boto3
import json
import logging
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pets')

def handler(event, context):

    unique_id = uuid.uuid4()
    
    payload = json.loads(event["body"])

    table.put_item(
        Item={
            'uuid': str(unique_id),
            'name': payload["name"],
            'breed': payload["breed"]
        }
    )

    return json.dumps({'uuid': str(unique_id)})
