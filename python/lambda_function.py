import json

# aws and dynamo libraries
import boto3

def lambda_handler(event, context):
    # dynamodb settings
    dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')
    tableName = "LOCATION"
    dynamodb_client = boto3.client('dynamodb')
    table = dynamodb.Table(tableName)
    response = table.put_item(
        Item = {
           'device_id': event['id'],
           'latitude': event['latitude']
        }
    )
    

    print("PutItem succeeded:")
    print(json.dumps(response, indent = 4))

    return {
        'statusCode': 200
    }