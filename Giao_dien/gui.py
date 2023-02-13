
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import PIL
from cProfile import label
from turtle import onclick
from tkinter import *
import subprocess
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2

from tkinter.ttk import *

from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import cv2

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets5")
window = Tk()

window.geometry("1200x700")
window.configure(bg = "#FFFFFF")
video_capture = cv2.VideoCapture(0)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def t():
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = PIL.ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.create_image(450.0, 200, anchor=tk.NW, image=imgtk)
    window.after(15, t)

        
          
def on_off():
    t()
def off_detect():
    return
     
def start_process():
    labelhienthi['text']=combo.get()
    if(labelhienthi['text']=='YOLOV5'):
       return
    elif(labelhienthi['text']=='YOLOV4'):
        return

def stop_process():
    if labelhienthi['text']=='YOLOV5' :
        return
    if labelhienthi['text']=='YOLOV4':
        return
        




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    750.0,
    350.0,
    image=image_image_1
)

canvas.create_text(
    108.0,
    129.0,
    anchor="nw",
    text="Menu ",
    fill="#000000",
    font=("UbuntuMono Regular", 70 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start_process,
    relief="flat"
)
button_1.place(
    x=12.0,
    y=228.0,
    width=176.0,
    height=56.0
)
combo = Combobox(window)
combo['values']=("YOLOV5","YOLOV4","MCNN")
combo.current(0)
combo.place(
    x=200.0,
    y=228.0,
    width=100,
    height=56
 
)
labelhienthi = Label(window,text='Not Select',font='Times 30')
labelhienthi.place(
    x=200.0,
    y=343.0,
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=12.0,
    y=343.0,
    width=176.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=12.0,
    y=458.0,
    width=176.0,
    height=56.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=on_off,
    relief="flat"
)
button_4.place(
    x=21.0,
    y=27.0,
    width=133.0,
    height=58.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=stop_process,
    relief="flat"
)
button_5.place(
    x=215.0,
    y=22.0,
    width=69.0,
    height=68.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1087.0,
    y=595.0,
    width=61.0,
    height=55.0
)


window.mainloop()