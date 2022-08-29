import glob
import os.path
import os
import time
'''
from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(
    ws,
    width = 500,
    height = 500
    )
canvas.pack()

folder_path = os.path.join(os.path.dirname(__file__), "templates")
file_type = r'\*.*'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

'''

folder_path = os.path.join(os.path.dirname(__file__), "image")
print(folder_path)
file_type = r'\*.*'
c = 0
while True:
  #  if [f for f in os.listdir(folder_path) if not f.startswith('.')] != []:
        # Some Work
        #files = glob.glob(folder_path + file_type)
        files = glob.glob(folder_path+ file_type)
        #afile=max(files, key=os.path.getctime)
        list_of_files = glob.glob(folder_path+ file_type) # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
       # max_file = max(files, key=os.path.getctime)
     #  print(max_file)
        c=c+1
        print(c)
        time.sleep(1)   # Its just to wait if 'Some Work' is very small
#    else:
  #      print('Empty')
   #     time.sleep(1)