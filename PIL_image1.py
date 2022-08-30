from PIL import Image
import glob
import os.path
import os
import time

folder_path = os.path.join(os.path.dirname(__file__), "image")
print(folder_path)
file_type = r'\*.jpg'
last=""
while True:
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    #read the image
    fp = open(max_file,"rb")
    im = Image.open(fp)
    if last != max_file:
        print(max_file)
        #show image
        im.show()
        #im.load()
        last=max_file
        time.sleep(1)
        fp.close()
        