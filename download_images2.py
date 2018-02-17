import boto3, os

#intiate s3 resource
s3 = boto3.resource('s3')

# select bucket
my_bucket = s3.Bucket('mango-pictures')

# download file into current directory
for object in my_bucket.objects.all():
    my_bucket.download_file(object.key, os.curdir+"/"+object.key)