import boto3
import os
import glob

#s3 = boto3.resource('s3')
#s3.Bucket('mydemobucket4767822315489').upload_file('/home/ec2-user/environment/s3Upload.py', 's3Upload.py') #Req: bucket name, file path and file name as the key


files = glob.glob("*.py") #uploads all files ending in .py with glob extentsion

for file in files: #for loop that uploads the files to the bucket
    s3 = boto3.resource('s3')
    s3.Bucket('mydemobucket4767822315489').upload_file(file, file) #bucket name (file,file) 

response = "file uploaded"

print(response)
