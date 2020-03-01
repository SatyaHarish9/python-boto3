import boto3
from pprint import pprint
ec2_res = boto3.resource(service_name="ec2", region_name="us-east-1")
#pprint(ec2_res.meta.client.describe_regions())
for each_item in ec2_res.meta.client.describe_regions()['Regions']:
    print (each_item['RegionName'],each_item['Endpoint'])
#print(dir(ec2_res))

