import boto3

s3_client = boto3.client('s3')

response = s3_client.list_buckets()
print(response['Buckets'])

for each in response['Buckets']:
    print(each['Name'])

#for Bucket in response['bucket']:
#    print(each[Bucket])
