from __future__ import print_function

import boto3
import json
import logging

log = logging.getLogger()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def handler(event, context):

    users = event["body"]

    for user in users:
        table.put_item(
            Item={
                'uuid': str(user["uuid"]),
                'gender': user["gender"],
                'email': user["email"],
                'ip_address': user["ip_address"],
                'timezone': user["timezone"],
                'first_name': user["first_name"],
                'last_name': user["last_name"]
            }
        )

    return json.dumps({'message': "Records added!"})
