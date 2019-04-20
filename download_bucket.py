


# For some reason this python script just downloads one folder and dies
# instead just run this on the command line from the directory you want to download to:
# aws s3 sync s3://mango-pictures .
# should be about 550 images

# download bucket
import boto3
from boto.s3.connection import S3Connection
import config
import os

AWS_ACCESS = config.key
AWS_SECRET = config.secret

s3client = boto3.client('s3')

bucket = 'mango-pictures'
# download_path = '/Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango/tmp'
download_path = '/Users/jonathanlittel/Dropbox/work/mazazul/testdata'


#print(s3client.list_objects(Bucket=bucket)['Contents'])

for obj in s3client.list_objects(Bucket=bucket)['Contents']:
    try:  
        filename = obj['Key'].rsplit('/', 1)[1]
        print(filename)
    except IndexError:
        print('error:')
        print(obj['Key'])
        filename = obj['Key']

    localfilename = os.path.join(download_path, filename)  # The local directory must exist.
    print(localfilename)
    s3client.download_file(bucket, obj['Key'], localfilename)