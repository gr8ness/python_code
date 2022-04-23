def terminate_ec2():
    print("deleting ec2")
    ec2=boto3.client('ec2')
    
    try:
        print("Terminating Instances")
        newlist=[]
        for reservation in ec2['Reservation']:
            for instance in reservation['Instances']:
                newlist.append(instance['InstanceId'])
            print(client.terminate_instances(IstanceIds=(newlist)))
    except:
            print("failed")
        
    
   
