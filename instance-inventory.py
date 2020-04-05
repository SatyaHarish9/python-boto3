import boto3
import csv

ec2_client = boto3.resource('ec2')

count = 1
csv_ob=open("inventory.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Private_Ip'])
for each in ec2_client.instances.all():
    print(count,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
    csv_w.writerow([count,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])
    count+=1
csv_ob.close()