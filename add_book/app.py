import json
import os
import uuid

import boto3


def put_book(title: str, author: str) -> dict:
    ddb = boto3.resource('dynamodb')

    table = ddb.Table(os.environ['BOOKS_TABLE_NAME'])
    response = table.put_item(
        Item={
            'id': uuid.uuid4().hex,
            'title': title,
            'author': author
        }
    )

    return response


def lambda_handler(event, context):
    payload = json.loads(event['body'])
    title = payload['title']
    author = payload['author']

    return {
        "statusCode": 200,
        "body": json.dumps(put_book(title, author)),
    }
