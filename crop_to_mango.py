# crop around the area where the mango is located

import os, sys
from PIL import Image

path = "/Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango"
os.chdir(path)
os.system('pwd')

# Batch re-crop all images
# resave them in the same folder (or a different one?) with the name train-jpg and test.jpg

files = os.listdir(f'{PATH}')


PATH = "data/raw/"
dirs = os.listdir( PATH )
# print(dirs)
def resize():
    for item in dirs:
        print(PATH+item)
        if os.path.isfile(PATH+item) and not item.startswith('.'):
            im = Image.open(PATH+item)
            f, e = os.path.splitext(PATH+item)
            area = (1000, 180, 2024, 1204) 
            im_crop = im.crop(area)
            im_crop.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
