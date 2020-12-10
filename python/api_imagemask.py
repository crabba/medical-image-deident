import boto3
import json

# Calls POST on /image/mask

client = boto3.client('apigateway') 

api_id = 'YOUR_API_ID'
resource_id = 'YOUR_IMAGEMASKRESOURCEID'
s3_bucket = 'YOUR_S3_IMAGE_BUCKET' 
s3_key = 'YOUR_S3_IMAGE_KEY'

destination_key = 'masked/' + s3_key
payload = {
    "phiDetectionThreshold": 0.5,
    "s3Bucket": s3_bucket,
    "s3Key": s3_key,
    "destinationBucket": s3_bucket,
    "destinationKey": destination_key
    }
response = client.test_invoke_method( 
    restApiId=api_id,
    resourceId=resource_id,
    httpMethod='POST',
    headers={"Content-Type": "application/json"}, 
    body=json.dumps(payload)
)

print(response['body'])
