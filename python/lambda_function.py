import json

# aws and dynamo libraries
import boto3

def lambda_handler(event, context):
    # dynamodb settings
    dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')
    tableName = "LOCATION"
    dynamodb_client = boto3.client('dynamodb')
    table = dynamodb.Table(tableName)

    # if id exists in db, it updates those values
    # if id does not exists in db, it just adds it with all the values comming from event
    # boards do not sent their geo-location. that's why these values are 'hardcoded' on db
    response = table.put_item(
        Item = {
           'device_id': event['id'],
           'latitude': '28.785969',
           'longitude': '-81.332263',
           'address': '363 Silver Pine Dr',
           'site': 'Lake Mary'
        }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent = 4))

    return {
        'statusCode': 200
    }