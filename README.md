## Some AWS Lambda examples.

### 1 `simple_pipeline_template` 

Implements a basic system for processing "orders".

The `submit_order.py` Lambda function accepts 'order' data via it's event, and creates a message which is placed on an SQS queue.
- The function could be triggered by AWS API Gateway.
- The `index.html` could be used for testing the system if hosted on a static web site (S3?) and set to use the API.

The `process_order.py` Lambda function reads messages from the queue and creates Order objects in a DynamoDB table.
- The function could be triggered by the SQS queue.

**Note:** This is meant to be a simple example for use as a template, and to demonstrate interaction with multiple AWS services.

### 2 `generate_test_data`

`package.zip` contains dependencies and a `lambda_function.py` file. This can generate random data which can be used for testing. The function is meant to be run manually using a Test Event. The event should simply contain the desired count of data records to create in the form: `{"Data Count": 100}`. The result is written to an S3 bucket.
- Random data is generated using [Faker](https://faker.readthedocs.io/en/master/index.html).
- The output format is JSON but can easily be changed.
- The current example data is "Profiles" (data about people). This should be changed to whatever is required. Faker has a huge number of providers.
- The Lambda function timeout will need to be increased. In testing, 1000 records took about 20 seconds.
- When implementing this function, it will need the necessary S3 permissions and the target bucket should be changed to the appropriate name.