import os
import json
import boto3

translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')
firehose = boto3.client('firehose')
TABLE_NAME = os.getenv('TABLE_NAME')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    response = {
        "statusCode": 200,
        "body":  json.dumps(result['Item']) 
    }


    return response