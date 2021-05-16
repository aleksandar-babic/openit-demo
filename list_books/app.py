import json
import os

import boto3


def list_books() -> list:
    ddb = boto3.resource('dynamodb')

    table = ddb.Table(os.environ['BOOKS_TABLE_NAME'])

    return table.scan()['Items']


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(list_books()),
    }
