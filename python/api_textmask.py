import boto3
import json

# Calls POST on /text/mask and invokes Lambda function `mask_text/lambda_function.py`

client = boto3.client('apigateway')

api_id = 'YOUR_API_ID'
resource_id = 'YOUR_TEXTMASKRESOURCEID'

payload = {
    "text": "PERSON INFORMATION\nName: SALAZAR, CARLOS\nMRN: RQ36114734\nED Arrival Time: 11/12/2011 18:15\nSex: Male\nDOB: 2/11/1961",
    "phiDetectionThreshold": 0.9
    }
response = client.test_invoke_method(
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='POST',
    headers={"Content-Type": "application/json"},
    body=json.dumps(payload))

print(response['body'])
