# crop around the area where the mango is located

import os, sys
from PIL import Image

# PATH = "/Users/jonathanlittel/Dropbox/work/mazazul/evaluamango/calimango"
PATH = "/home/jupyter/calimango"
os.chdir(PATH)
os.system('pwd')

# Batch re-crop all images
# resave them in the same folder (or a different one?) with the name train-jpg and test.jpg

files = os.listdir(PATH)
# files = os.listdir(f'{PATH}')

print(files[0:10])
print('break')
print(os.getcwd())
# print(files)

def resize(PATH, path_out, name):
    dirs = os.listdir( PATH )
    for item in dirs:
        print(PATH+item)
        if os.path.isfile(PATH+item) and not item.startswith('.'):
            im = Image.open(PATH+item)
            f, e = os.path.splitext(PATH+item)
            print(f)
            print(e)
            area = (1000, 180, 2024, 1204) 
            im_crop = im.crop(area)
            # im_crop.save(f + ' resized.jpg', 'JPEG', quality=90)
            im_crop.save(path_out + '/' + name + "_" + item, 'JPEG', quality=90)


# resize(PATH = "data/raw/")
PATH_OUT = "/home/jupyter/calimango/data/resized/"
resize(PATH = "data/single_phillip_front/", path_out = PATH_OUT, name = 'multi')
resize(PATH = "data/single_phillip_back/", path_out = PATH_OUT, name = 'multi')
resize(PATH = "data/single_maz_front_2/", path_out = PATH_OUT, name = '2')
resize(PATH = "data/single_maz_front_1/", path_out = PATH_OUT, name = '1')
resize(PATH = "data/single_maz_back_2/", path_out = PATH_OUT, name = '2')
resize(PATH = "data/single_maz_back_1/", path_out = PATH_OUT, name = '1')

# ls data/single_phillip_front/

# ls data/resized/