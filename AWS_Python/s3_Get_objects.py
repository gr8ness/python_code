import boto3


s3_resource = boto3.client('s3')

objects = s3_resource.list_objects(Bucket = "mydemobucket4767822315489")["Contents"] #turn resource name into a variable to invoke s3


len(objects)
if len(objects) > 0:
    print("object exits")

for object in objects:
    print(object["Key"])
    
