    
    
import os
import json
import boto3

translate = boto3.client('translate')
dynamodb = boto3.client('dynamodb')
firehose = boto3.client('firehose')
TABLE_NAME = os.getenv('TABLE_NAME')

def funcion(language):
    id = "lkjlfksjd"
    trans = translate.translate_text(Text="Hello",
                 SourceLanguageCode='en', TargetLanguageCode=language)

    response = {
        "statusCode": 200,
        "body":  json.dumps(trans.get('TranslatedText')) 
    }


    return response
    
print(funcion("de"))