import boto3
image = raw_input("Enter the image id \n")
instance_type = raw_input("Enter the instance type \n")
key = raw_input("Enter the key \n")
user_data = ''' #!/bin/bash
yum update -y
amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
yum install -y httpd mariadb-server
systemctl start httpd
systemctl enable httpd
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php'''

ec2_client = boto3.client('ec2')
response = ec2_client.run_instances(
        ImageId=str(image),
        InstanceType=str(instance_type),
        KeyName=str(key),
        UserData = user_data,
        MaxCount=2,
        MinCount=1
)