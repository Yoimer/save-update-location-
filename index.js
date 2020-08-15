/*
    this function saves or updates values on LOCATION
    if id is already on LOCATION it updates it
    if id is new, it just adds it

    event example for test
    {
        "id": "TG2",
        "latitude": "28.785969"
    }
*/

// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');

// Set the region 
AWS.config.update({
    region: 'us-west-2'
});

// Create the DynamoDB service object
var ddb = new AWS.DynamoDB({
    apiVersion: '2012-08-10'
});

exports.handler = (event, context, callback) => {
    console.log('Received event:', JSON.stringify(event, null, 2));

    var params = {
        TableName: 'LOCATION',
        Item: {
            'device_id': {
                S: event.id
            },
            'latitude': {
                S: event.latitude
            }
        }
    };

    // Call DynamoDB to add the item to the table
    ddb.putItem(params, function (err, data) {
        if (err) {
            console.log("Error", err);
        } else {
            console.log("Success", data);
        }
    });
}