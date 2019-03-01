# download images from S3
import sys, os, glob, time
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import boto3
import config

AWS_ACCESS = config.key
AWS_SECRET = config.secret

conn = S3Connection(AWS_ACCESS,AWS_SECRET)
bucket = conn.get_bucket('mango-pictures')


def download_dir(client, resource, dist, local='/tmp', bucket='mango-pictures'):
    paginator = client.get_paginator('list_objects')
    # print(paginator)
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                # download_dir(client, resource, subdir.get('Prefix'), local, bucket)
                print(subdir)
        if result.get('Contents') is not None:
            for file in result.get('Contents'):
                if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
                     os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
                     if not file.get('Key').endswith('/'):
                     	resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))

# def download_dir(client, resource, dist, local='/tmp', bucket='mango-pictures'):
#     paginator = client.get_paginator('list_objects')
#     for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
#         if result.get('CommonPrefixes') is not None:
#             for subdir in result.get('CommonPrefixes'):
#                 download_dir(client, resource, subdir.get('Prefix'), local, bucket)
#         if result.get('Contents') is not None:
#             for file in result.get('Contents'):
#                 if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
#                      os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
#                 resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))

# if not file.get('Key').endswith('/')


def _start():
    client = boto3.client('s3')
    resource = boto3.resource('s3')
    # download_dir(client, resource, subdir.get('Prefix'), local='/tmp', bucket='mango-pictures')
    download_dir(client, resource, dist='', local='Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango/tmp')

_start()


# client = boto3.client('s3')
# resource = boto3.resource('s3')
# download_dir(client, resource, 'clientconf/', '/tmp')

# note
# Amazon S3 does not have folders/directories. It is a flat file structure.
# To maintain the appearance of directories, path names are stored as part of the object Key (filename). For example:
# images/foo.jpg

# s3=boto3.client('s3')
# list=s3.list_objects(Bucket='mango-pictures')['Contents']

# aws cli command:
# aws s3 sync SRC s3://BUCKET_NAME/DIR[/DIR....]
# aws s3 sync SRC s3://mango-pictures/single_phillip_back
# aws s3 sync tmp s3://mango-pictures/single_phillip_back
# aws s3 sync /Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango/data s3://mango-pictures/single_phillip_back
# aws s3 sync s3://mango-pictures/single_phillip_back /Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango/data 
