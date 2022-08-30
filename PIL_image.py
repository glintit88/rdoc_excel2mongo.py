from PIL import Image
import glob
import os.path
import os
import time

folder_path = os.path.join(os.path.dirname(__file__), "image")
print(folder_path)
file_type = r'\*.jpg'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
#read the image
im = Image.open(max_file)

#show image
im.show()

time.sleep(1)
im.close()