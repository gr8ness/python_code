"""
Your module description
"""
import boto3

client = boto3.client('ec2')

def start_instance():
    try:
        print("start instance")
        response = client.start_instances(
        InstanceIds=[ #provide instance ids
            'i-0660aee66332ebfbc','i-0ad3832008a2720bf' 
        ],
    )
    
    for instance in InstanceIds:
        
    
    except:
        print("failed")
start_instance()
