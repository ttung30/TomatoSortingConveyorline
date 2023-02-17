import PIL
from cProfile import label
from turtle import onclick
import subprocess
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import cv2
from threading import Thread, Lock
from pathlib import Path
import torch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets5")


on = 0
start = None
stop = None
window = Tk()
video_capture = None
window.geometry("1200x700")
window.configure(bg = "#FFFFFF")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)  
def on_off():
    global video_capture 
    video_capture=cv2.VideoCapture(0)
    #write uart tat he thong
def start_process():
    global stop
    global start
    stop = 0
    start =1
    yolo()  
def yolo():
    textpush = ''
    color = ''
    label = ['ca chua','keo']
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    result = yolo_model(cv2image)
    g=result.xyxy[0].tolist()
    if g!= [] and stop == 0:
        index = int(g[0][5])
        textpush='Ca chua loai: '+label[index]
        color =(0, 0, 255)
    if stop == 1:
        textpush = ' He thong tam dung hoat dong!'
        color = (255, 0, 0)
    
    cv2.putText(cv2image, textpush, (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1, color, 2)
    img = PIL.Image.fromarray(cv2image)
    imgtk = PIL.ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.create_image(450.0, 200, anchor=tk.NW, image=imgtk)
    if stop == 1 and start ==0:
        return
    window.after(1, yolo)
    
def stop_dectect():
    global stop 
    global start
    stop=1
    start =0
    #write uart dung phan loai 
def stop_process():
    messagebox.showinfo('Shutdown', "He thon se dung sau 3s")
    #write uart  he thong ngung hoat dong
    time.sleep(3)
    window.destroy()
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
    command=stop_dectect,
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

if __name__ =="__main__":
    yolo_model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
    t1=Thread(target=window.mainloop())
    t1.start()
