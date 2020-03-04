import boto3
ec2_client = boto3.client('ec2')
for each_vol in ec2_client.describe_volumes()['Volumes']:
    #print(each_vol['VolumeId'])
    if each_vol['State'] == 'available':
        print(each_vol['VolumeId'])
        print("Deleting the volumes")
        ec2_client.delete_volume(VolumeId=each_vol['VolumeId'])