from __future__ import print_function

import os, sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../../"))
sys.path.append(os.path.join(here, "../../vendored"))

import lib

table = lib.users_table()

def handler(event, context):

    response = table.scan()

    return response['Items']
