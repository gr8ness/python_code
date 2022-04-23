"""
Your module description
"""

import boto3
import glob
import os

s3_resource = boto3.client('s3')

s3_resource.delete_objects(Bucket = "mydemobucket4767822315489", Delete = {'Objects': [{'Key': '*.py'}]}) 

#files = s3_resource.list_objects(Bucket = "mydemobucket4767822315489")["Contents"]
files = glob.glob("*.py")  


for object in files:
    response = s3_resource.delete_objects(Bucket = "mydemobucket4767822315489", Delete = {'Objects': [{'Key': '*.py'}]})
    Key = (object["Key"])
    print(response)
