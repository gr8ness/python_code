"""
Your module description
"""
import boto3

client=boto3.client('ec2')

def stop_instance():
    try:
        print("stop instance")
        response = client.stop_instances(
            InstanceIds=[
                'ENTER_INSTANCE_ID','ENTER_INSTANCE_ID',
            ],
            #Hibernate=True|False,
        )
    except:
        print("failed")
        
stop_instance()
