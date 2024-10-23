import json
import boto3

sqs = boto3.client("sqs")

# Replace the below queue uri
QUEUE_URI = "<SQS QUEUE URI>"

def lambda_handler(event, context):
    try:
        order_detail = json.loads(event["body"])
        response = sqs.send_message(
            QueueUrl=QUEUE_URI,
            MessageBody=json.dumps(order_detail)
        )
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return {
        "statusCode": 200,
        # May need to include headers such as:
        # "headers": {
        #     "Access-Control-Allow-Origin": "*",
        #     "Access-Control-Allow-Headers": "Content-Type",
        #     "Access-Control-Allow-Methods": "OPTIONS,POST"
        # },
        "body": json.dumps({"message": "Order submitted"})
    }
