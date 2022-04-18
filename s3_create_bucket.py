"""
using boto3 and python to create an s3 bucket
"""
import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("demobucket2387094359034")

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)
print(response)
