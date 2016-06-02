from __future__ import print_function

import boto3
import json
import logging
from boto3.dynamodb.conditions import Key, Attr

log = logging.getLogger()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pets')

def handler(event, context):

    response = table.scan()

    items = response['Items']

    print(items)

    return items
