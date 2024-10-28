### A simple AWS Lambda example.

Implements a basic system for processing "orders".

The `submit_order.py` Lambda function accepts 'order' data and creates a message which is placed on an SQS queue.
- The function could be triggered by AWS API Gateway.
- The `index.html` could be used for testing the system if hosted on a static web site (S3?) and set to use the API.

The `process_order.py` Lambda function reads messages from the queue and creates Order objects in a DynamoDB table.
- The function could be triggered by the SQS queue.

**Note:** This is meant to be a simple example for use as a template, and to demonstrate interaction with multiple AWS services.