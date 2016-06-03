from __future__ import print_function

import os, sys, json

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../../"))
sys.path.append(os.path.join(here, "../../vendored"))

import lib

table = lib.users_table()

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
