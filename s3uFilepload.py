import boto3
import os

s3 = boto3.resource('s3')
s3.Bucket('mydemobucket4767822315489').upload_file('/home/ec2-user/environment/s3Upload.py', 's3Upload.py') #Req: bucket name, file path and file name as the key

response = "file uploaded"

print(response)
