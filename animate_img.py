import time
import tkinter
from PIL import Image, ImageTk
class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tkinter.Canvas(master, width=400, height=400,  bg= "#2D572C", highlightthickness= 0)
        self.canvas.place(x=169,y=249)
        self.process_next_frame = self.draw().__next__  # Using "next(self.draw())" doesn't work
        master.after(1, self.process_next_frame)
    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        print(self.process_next_frame)
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(200, 200, image=tkimage)
            self.master.after_idle(self.process_next_frame)
            yield
            self.canvas.delete(canvas_obj)
            angle += 1
            angle %= 360
            time.sleep(0.002)