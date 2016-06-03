from __future__ import print_function

import boto3
import json
import logging
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def handler(event, context):

    unique_id = uuid.uuid4()
    user = event["body"]

    table.put_item(
        Item={
            'uuid': str(unique_id),
            'gender': user["gender"],
            'email': user["email"],
            'ip_address': user["ip_address"],
            'timezone': user["timezone"],
            'first_name': user["first_name"],
            'last_name': user["last_name"]
        }
    )

    return json.dumps({'uuid': str(unique_id)})
