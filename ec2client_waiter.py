import boto3

ec2_client = boto3.client(service_name="ec2", region_name="us-east-1")
response = ec2_client.start_instances(InstanceIds=['i-02d8ce2d06a40dcbf'])
#print(response)
print("Starting the ec2 instance{}".format('i-02d8ce2d06a40dcbf'))
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-02d8ce2d06a40dcbf'])
print("Instance has started")







