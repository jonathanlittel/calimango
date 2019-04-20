for obj in s3client.list_objects(Bucket=bucket)['Contents']:
#     try:  
#         filename = obj['Key'].rsplit('/', 1)[1]
#         print(filename)
#     except IndexError:
#         filename = obj['Key']

#     localfilename = os.path.join(download_path, filename)  # The local directory must exist.
#     print(localfilename)
#     s3client.download_file(bucket, obj['Key'], localfilename)