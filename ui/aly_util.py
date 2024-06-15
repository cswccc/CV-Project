import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, font

from mode1 import Ver
from utils.FaceRec import FaceRec
from utils.ImageProcess import *
import cv2 as cv
faceRec = FaceRec("ArcFace")
def select_file():
    print("select")
    file_path = filedialog.askopenfilename()
    return file_path

def show(image_label,info_label,aly):
    global image_show
    global info_show
    info_show = ""
    selected_file = select_file()
    print(selected_file)
    face_aly = imageRead(selected_file)
    result = faceRec.analyzeFace(face=face_aly)
    out = face_aly.copy()
    if len(result) == 0:
        info_show += "检测不到人脸"
    else:
        for idx, r in enumerate(result):
            info = 'ID: ' + str(idx) + ' ' + r['emotion'] + ' ' + r['gender'] + ' ' + str(r['age'])
            out = drawRectangle(out, r['box'], additionInfo=info)
            info_show += info + '\n'
    # Load an image
    out = cv.cvtColor(out, cv.COLOR_BGR2RGB)
    image = Image.fromarray(out)
    pi = image.size[1] / image.size[0]
    if pi < 1:
        image = image.resize((500, int(pi * 500)))
    else:
        image = image.resize((int(1 / pi * 500), 500))
    image_show = ImageTk.PhotoImage(image)

    # Create a label to display the image

    image_label.config(image=image_show)
    image_label.place(x=200, y=300)
    info_font = font.Font(family="Helvetica", size=30)
    info_label.config(font=info_font)
    info_label.config(text=info_show)
    info_label.place(x=800, y=300)

    print("show over")
    aly.mainloop()

def aly_w(aly,root,back):
    print("aly")
    root.withdraw()

    aly.deiconify()
    # max
    aly.state('zoomed')
    image = Image.open("bg.jpg")  # 请将此处替换为您的图片路径
    image.putalpha(128)
    image = image.resize((1900, 1000))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(aly, image=photo)
    label.pack(fill=tk.BOTH, expand=True)
    # Start the Tkinter event loop
    image_label = tk.Label(aly)
    info_label = tk.Label(aly, bg="green")
    custom_font = font.Font(family="Helvetica", size=20)
    button_b = tk.Button(aly, text="back", font=custom_font, width=10, height=5, bg="green", command=lambda: back(aly,image_label,info_label))
    button_b.place(x=0, y=0)

    label_font = font.Font(family="Helvetica", size=30)
    text_label = tk.Label(aly, text="欢迎使用人脸分析功能", font=custom_font, width=20, height=4, bg="green")
    text_label.place(x=725, y=0)


    button_select = tk.Button(aly, text="选择图片", font=custom_font, width=10, height=3, bg="green", command=lambda: show(image_label,info_label,aly))
    button_select.place(x=800, y=150)
    aly.mainloop()
