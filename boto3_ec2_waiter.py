import boto3
import time

aws_con = boto3.session.Session()
ec2_res = aws_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con = aws_con.client(service_name="ec2", region_name="us-east-1")

my_inst = ec2_res.Instance('i-02d8ce2d06a40dcbf')
#print(dir(ec2_res))
print("starting the ec2 instance ")
my_inst.start()
#print(my_inst)
# Resource waiter waits for 200sec(40 checks after every 5 seconds)
my_inst.wait_until_running()
print("The instance{} has started".format(my_inst.id))



