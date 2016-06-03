from __future__ import print_function

import os, sys
from pprint import pprint

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../../"))
sys.path.append(os.path.join(here, "../../vendored"))

import lib

table = lib.users_table()

def handler(event, context):

    response = table.get_item(
        Key={
            'uuid': str(event["uuid"])
        }
    )

    if response.has_key("Item"):
        return response["Item"]
    else:
        raise Exception("[BadRequest] UUID not found")
