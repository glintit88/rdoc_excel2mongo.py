import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image
import time

images = ["image/t2.jpg", "image/test.png", "image/1.png"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def slideShow():
  #time.sleep(1)   
  img = next(photos)
  #img = ImageTk.PhotoImage(Image.open(image/test.png))  
  print(img)
  displayCanvas.config(image=img)
  root.after(1000, slideShow) # 0.05 seconds

root = tk.Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenwidth()
root.geometry('%dx%d' % (640, 480))
displayCanvas = tk.Label(root)
displayCanvas.pack()
root.after(1000, lambda: slideShow())

root.mainloop()