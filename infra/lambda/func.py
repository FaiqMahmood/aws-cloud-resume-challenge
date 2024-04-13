import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-tablle')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'ID': '1'
    })
    view = response['Item']['views']
    views = view + 1
    print(views)
    response = table.put_item(Item={
        'ID': '1',
        'views': views
    })
    
    return views