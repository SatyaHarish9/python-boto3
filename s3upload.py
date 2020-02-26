import boto3
import logging
from botocore.exceptions import ClientError

#creating s3 client to interact with s3
s3_client = boto3.client('s3')

# upload_file() method accepts the parameters file_name, S3 bucket and object_name
s3_client.upload_file('contacts.csv', 'harideepdive', 'contacts.csv')




