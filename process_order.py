import json
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
# Replace the table name below
TABLE_NAME = "<DYNAMODB TABLE NAME>"
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        for record in event["Records"]:
            message_body = json.loads(record["body"])
            item = {
                # Use the SQS messageId as the orderId?
                "orderId": record["messageId"],
                "productName": message_body["productName"],
                "quantity": message_body["quantity"],
                "orderDate": datetime.now().isoformat()
            }
            table.put_item(Item=item)
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"{len(event["Records"])} order(s) processed successfully"})
    }
