from __future__ import print_function

import boto3
import json
import logging
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pets')

def handler(event, context):

    unique_id = uuid.uuid4()

    table.put_item(
        Item={
            'uuid': str(unique_id),
            'name': event["body"]["name"],
            'breed': event["body"]["breed"]
        }
    )

    return json.dumps({'uuid': str(unique_id)})
