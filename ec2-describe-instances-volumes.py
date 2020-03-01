import boto3
from pprint import pprint
ec2_console = boto3.client('ec2')

response = ec2_console.describe_instances()['Reservations']
for each_item in response:
    for each in each_item['Instances']:
        print("The image Id is: {}\nThe Instance Id is: {}\n".format(each['ImageId'],each['InstanceId']))
    print(each_item['Instances'])

response1 = ec2_console.describe_volumes()['Volumes']
for each_item in response1:
    print("===================")
    print("The volume id is: {}\nThe Availability zone is: {}\nThe VolumeType is:{}\n".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))