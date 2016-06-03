import boto3, os, sys, json, logging

def users_table():
    dynamodb = boto3.resource('dynamodb')
    return dynamodb.Table('users')

def get_logger():
    return logging.getLogger()
