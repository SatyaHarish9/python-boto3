import csv
import boto3

with open('persons.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Derek', 'Software Developer'])
    filewriter.writerow(['Steve', 'Software Developer'])
    filewriter.writerow(['Paul', 'Manager'])

s3_client = boto3.client('s3')
def lambda_handler(event,context):
#    with open("persons.csv", "rb") as f:
#        s3_client.upload_fileobj(f, "harideepdive", "persons.csv")
#    s3_client.upload_file('ourpersons.csv', 'harideepdive', 'ourpersons.csv')
    try:
        s3_response = s3_client.put_object(Bucket='harideepdive', Key='/Users/sgumpall/Documents/python/boto3/python-boto3')
    except Exception as e:
        raise IOError(e)
    return {
        'statusCode': 200,
        'body': {
            'file_path': /Users/sgumpall/Documents/python/boto3/python-boto3
        }
    }

