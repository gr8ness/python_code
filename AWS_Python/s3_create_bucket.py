"""
using boto3 and python to create an s3 bucket NOTE: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket
"""
import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("BUCKET_NAME")

response = bucket.create(
    ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
    CreateBucketConfiguration={     #delete to have bucket deployed in default region us-east-1
        'LocationConstraint': 'REGION' 
    },
    
)
print(response)
