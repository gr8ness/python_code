"""
Your module description
"""
import boto3

client=boto3.client('ec2')

def create_ec2():
    try:
        print('Creating EC2 instance')
        ec2=boto3.client('ec2')
        ec2.run_instances(
            ImageId='ami-0f9fc25dd2506cf6d',
            MinCount=2, 
            MaxCount=2, #creates instances with min and max. add image ID and instance type
            InstanceType='t2.micro',
            #KeyName='ec2-keypair' #add a key pair to ssh into instance
            SecurityGroups=['default']
            UserData= #add a script
            #tags=[{'ResourceType': 'instance','Key': }]
            )
            
    except:
        print("Failed")
    
create_ec2()
