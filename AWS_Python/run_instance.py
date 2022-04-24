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
            'ENTER_INSTANCE_ID','ENTER_INSTANCE_ID' 
        ],
    )
    
    for instance in InstanceIds:
        
    
    except:
        print("failed")
start_instance()
