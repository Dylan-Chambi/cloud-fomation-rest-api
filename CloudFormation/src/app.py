import json

def lambda_handler(event, context):
    body = event['body']
    print(body)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }