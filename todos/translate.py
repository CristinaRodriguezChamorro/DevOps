import os
import json

import boto3
translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')
firehose = boto3.client('firehose')
TABLE_NAME = os.getenv('TABLE_NAME')

def lambda_handler(event, context):

    # fetch todo from the database
    id = event['pathParameters']['id']
    language = event['pathParameters']['language']
    trans = translate.translate_text(Text="Hello",
             SourceLanguageCode='en', TargetLanguageCode=language)

    responses = {
        "statusCode": 200,
        "body":  json.dumps(trans.get('TranslatedText')) 
    }
    return response