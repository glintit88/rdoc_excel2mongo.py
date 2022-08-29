import glob
import os.path
import time
import os
from tkinter import *      
from PIL import ImageTk,Image
import webbrowser


def loop1():
    folder_path = 'C:\\Users\\terencema\\Desktop\\MouseWithoutBorders\\image'
    file_type = r'\*.jpg'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    print (folder_path)
    c = 0
    new =1
    url = "https://www.pythgonguides.com"
    
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
        print(img)
        time.sleep(1)   # Its just to wait if 'Some Work' is very small
    else:
        print('Empty')
        time.sleep(1)

def openbrowser():
    url = "https://www.pythonguides.com"
    webbrowser.open(url,new=1)

#bg = PhotoImage(file = 'image/test.png')


ws = Tk()
ws.title('RDOC Login')
ws.geometry('500x500')

canvas = Canvas(
    ws,
    width = 500, 
    height = 500
    )      
canvas.pack(fill='both', expand = True)

'''
canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)
'''
canvas.create_text(
	250, 
	150, 
	text = 'RDOC Info',
	font=('Arial', 50),
	)

btn = Button(
	ws, 
	text = 'EXPLORE MORE',
	command=openbrowser,
	width=20,
	height=2,
	relief=SOLID,
	font=('arial', 18)
	)

btn_canvas = canvas.create_window(
	100, 
	200,
	anchor = "nw",
	window = btn,
	)


loop1()
#folder_path = os.path.join(os.path.dirname(__file__), "image")
#folder_path = os.getcwd()
ws.mainloop()

