import boto3
import sys
ec2_client = boto3.client(service_name="ec2", region_name="us-east-1")
ec2_resource = boto3.resource(service_name="ec2", region_name="us-east-1")

while True:
    print("Following actions can be performed on the EC2 instance")
    print(""" 
    1. start
    2. stop 
    3. Terminate 
    4. Exit""")

    opt = int(input("Enter the operation to be performed: "))
    if opt==1:
        instance_Id=input('Enter the instanceId to start: ')
        instance = ec2_resource.Instance('instance_Id')
        print(dir(instance))
        print("Starting the ec2 instance")
        instance.start()
    elif opt==2:
        instance_Id = input("Enter the instanceId to stop: ")
        instance = ec2_resource.Instance('instance_Id')
        print("Stopping the ec2 instance")
        instance.stop()

    elif opt==3:
        instance_Id = input("Enter the instanceId to start\n")
        instance = ec2_resource.Instance('instance_Id')
        print("terminating the ec2 instance")
        instance.terminate()

    elif opt==4:
        print("Thank you for using this script")
        sys.exit()
    else:
        print("Your option is invalid. Please try again")
    
