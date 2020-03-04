import boto3
ec2_client=boto3.resource('ec2')
f1 = [{'Name': 'status', 'Values':['available'] }]
for each_vol in ec2_client.volumes.filter(Filters=f1):
    print(each_vol.id)
    print("Deleting the unused volumes")
    each_vol.delete()


