import os

# question - set up file structure on AWS, or moving around w/ script?

# Download all files from S3 bucket

PATH = "data/mango/"

!aws s3 sync s3://mango-pictures/ /home/paperspace/calimango/data 
!mk 

# TODO add sample folder for testing

# make train, test, and validation folders, with folders for each classification inside


source_files = '/PATH/TO/FOLDER/*'
destination_folder = 'PATH/TO/FOLDER'
# equivalent of $ mv source_files destination_folder

os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo")
