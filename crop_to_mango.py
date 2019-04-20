# crop around the area where the mango is located

import os, sys
from PIL import Image

PATH = "/Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango"
os.chdir(PATH)
os.system('pwd')

# Batch re-crop all images
# resave them in the same folder (or a different one?) with the name train-jpg and test.jpg

files = os.listdir(PATH)
# files = os.listdir(f'{PATH}')

print(files[0:10])
print('break')
print(files)

def resize(PATH):
    dirs = os.listdir( PATH )
    for item in dirs:
        print(PATH+item)
        if os.path.isfile(PATH+item) and not item.startswith('.'):
            im = Image.open(PATH+item)
            f, e = os.path.splitext(PATH+item)
            area = (1000, 180, 2024, 1204) 
            im_crop = im.crop(area)
            im_crop.save(f + ' resized.jpg', 'JPEG', quality=90)

# resize(PATH = "data/raw/")
resize(PATH = "data/single_phillip_front/")
resize(PATH = "data/single_phillip_back/")
resize(PATH = "data/single_maz_front_2/")
resize(PATH = "data/single_maz_front_1/")
resize(PATH = "data/single_maz_back_2/")
resize(PATH = "data/single_maz_back_1/")