import boto3
import datetime

day = str(datetime.datetime(2019, 10, 11, 5, 00, 27))
print(day)
ec2_client = boto3.resource('ec2')
response = ec2_client.snapshots.all()
for each in response:
    if each.start_time.strftime("%Y-%m-%d %H:%M:%S") == day:
        print(each.id,each.start_time.strftime("%Y-%m-%d %H:%M:%S"))
