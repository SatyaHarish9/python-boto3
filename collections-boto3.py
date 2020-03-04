import boto3

ec2_client = boto3.resource(service_name="ec2")
print(ec2_client.instances.all())
f1 = [ { 'Name':'instance-state-name', 'Values':['running'] }, { 'Name': 'instance-type', 'Values':['t2.micro']}]
for each in ec2_client.instances.filter(Filters=f1):
    print(each)

