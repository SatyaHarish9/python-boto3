import boto3
#creating the sts client to interact with sts
sts_client = boto3.client('sts')
response = sts_client.get_caller_identity()

#Response returns the dictionary object so we are filtering for Account Id.
print(response['Account'])