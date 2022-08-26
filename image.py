import glob
import os.path
import time
import os
from tkinter import *      
from PIL import ImageTk,Image

ws = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(
    ws,
    width = 500, 
    height = 500
    )      
canvas.pack()

#folder_path = os.path.join(os.path.dirname(__file__), "image")
#folder_path = os.getcwd()
folder_path = 'C:\\Users\\terencema\\Desktop\\MouseWithoutBorders\\image'
file_type = r'\*.jpg'
files = glob.glob(folder_path + file_type)

max_file = max(files, key=os.path.getctime)
print (folder_path)
c = 0
while True:
    if [f for f in os.listdir(folder_path) if not f.startswith('.')] != []:
        # Some Work
        canvas = Canvas(
            ws,
            width = 500, 
            height = 500
            )      
        canvas.pack()

        files = glob.glob(folder_path + file_type)
        max_file = max(files, key=os.path.getctime)
        print(max_file)
        c=c+1
        print(c)
        img = ImageTk.PhotoImage(Image.open(max_file))  
        canvas.create_image(
                10, 
                10, 
                anchor=NW, 
                image=img
                )
        canvas.pack()
        ws.mainloop()

        time.sleep(1)   # Its just to wait if 'Some Work' is very small
    else:
        print('Empty')
        time.sleep(1)


ws.mainloop()
