import tkinter
from PIL import Image, ImageTk
counter = 1

class Wheel(object):
    counter =0
    def __init__(self,window):
        self.window = window
        self.image = Image.open('img/wheel.png')
        self.tkimage = ImageTk.PhotoImage(self.image)
        self.label = tkinter.Label(self.window, image=self.tkimage)
        self.label.configure(bg='#2D572C')
        self.label.place(x=300,y=250)
        
    
    def rotate(self):
        global image, tkimage
        image = Image.open('img/wheel.png')
        image = image.rotate(self.counter)
        tkimage = ImageTk.PhotoImage(image)
        self.label.configure(image=tkimage,)
        self.counter += 1
        self.counter %= 360
        if self.counter<120:
            self.window.after(10, self.rotate)
        