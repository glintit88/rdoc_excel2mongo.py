import glob
import os.path
import time

folder_path = os.path.join(os.path.dirname(__file__), "templates")
file_type = r'\*.*'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

print(max_file)
c = 0
while True:
    if [f for f in os.listdir(folder_path) if not f.startswith('.')] != []:
        # Some Work
        files = glob.glob(folder_path + file_type)
        max_file = max(files, key=os.path.getctime)
        print(max_file)
        c=c+1
        print(c)
        time.sleep(1)   # Its just to wait if 'Some Work' is very small
    else:
        print('Empty')
        time.sleep(1)