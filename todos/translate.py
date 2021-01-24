import os
import json
import boto3

translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')
firehose = boto3.client('firehose')
TABLE_NAME = os.getenv('TABLE_NAME')

def translate_handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    text = result['Item']['text']
    language =  event['pathParameters']['id']
    trans = translate.translate_text(Text=text,
                 SourceLanguageCode='en', TargetLanguageCode=language)

    response = {
        "statusCode": 200,
        "body":  json.dumps(trans.get('TranslatedText')) 
    }


    return response