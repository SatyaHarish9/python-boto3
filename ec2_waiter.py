import boto3
import time

aws_con = boto3.session.Session()
ec2_res = aws_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con = aws_con.client(service_name="ec2", region_name="us-east-1")

my_inst = ec2_res.Instance('i-02d8ce2d06a40dcbf')
#print(dir(ec2_res))
print("starting the ec2 instance ")
my_inst.start()
#print(my_inst.state['Name'])

while True:
    my_inst = ec2_res.Instance('i-02d8ce2d06a40dcbf')
    if my_inst.state['Name']=="running":
        break
    print("Waiting for the instance to get into running state")
    time.sleep(15)

print("The instance{} has started".format(my_inst))



