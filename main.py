import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, font

from FaceRec import FaceRec
from ImageProcess import *
import cv2 as cv

# .withdraw()  隐藏窗口
# .deiconify() 显示窗口


root = tk.Tk()
reg = tk.Tk()

reg.title("reg")
reg.withdraw()
cmp = tk.Tk()
cmp.title("cmp")
cmp.withdraw()
aly = tk.Toplevel()
aly.title("aly")
aly.withdraw()

#for aly
image_show = None
info_show = ""
faceRec = FaceRec("ArcFace")

#关闭设置
def on_closing():
    # 在这里可以添加一些清理操作，例如保存数据等
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
reg.protocol("WM_DELETE_WINDOW", on_closing)
cmp.protocol("WM_DELETE_WINDOW", on_closing)
aly.protocol("WM_DELETE_WINDOW", on_closing)



def back(win):
    root.deiconify()
    root.state('zoomed')
    win.withdraw()


def select_file():
    print("select")
    file_path = filedialog.askopenfilename()
    return file_path


def show():
    global image_show
    global info_show
    info_show = ""
    selected_file = select_file()
    print(selected_file)
    face_aly = imageRead(selected_file)
    result = faceRec.analyzeFace(face=face_aly)
    out = face_aly.copy()
    for idx, r in enumerate(result):
        info = 'ID: ' + str(idx) + ' ' + r['emotion'] + ' ' + r['gender'] + ' ' + str(r['age']) + '\n'
        out = drawRectangle(out, r['box'], additionInfo=info)
        info_show += info

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

    image_label = tk.Label(aly, image=image_show)
    image_label.place(x=200, y=300)
    info_font = font.Font(family="Helvetica", size=30)
    image_label = tk.Label(aly, font=info_font, bg="green", text=info_show)
    image_label.place(x=800, y=300)

    print("show over")


def reg_w():
    print("reg")
    root.withdraw()
    reg.deiconify()
    # max
    reg.state('zoomed')
    # Start the Tkinter event loop
    button_b = tk.Button(reg, text="back", command=lambda: back(reg))
    button_b.pack(pady=10)
    reg.mainloop()


def cmp_w():
    print("cmp")
    root.withdraw()
    cmp.deiconify()
    # max
    cmp.state('zoomed')
    # Start the Tkinter event loop
    button_b = tk.Button(cmp, text="back", command=lambda: back(cmp))
    button_b.pack(pady=10)
    cmp.mainloop()


def aly_w():
    print("aly")
    root.withdraw()

    aly.deiconify()
    # max
    aly.state('zoomed')
    image = Image.open("bg_image/bg.jpg")  # 请将此处替换为您的图片路径
    image.putalpha(128)
    image = image.resize((1900, 1000))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(aly, image=photo)
    label.pack(fill=tk.BOTH, expand=True)
    # Start the Tkinter event loop
    custom_font = font.Font(family="Helvetica", size=20)
    button_b = tk.Button(aly, text="back", font=custom_font, width=10, height=5, bg="green", command=lambda: back(aly))
    button_b.place(x=0, y=0)

    image_label = tk.Label(aly, text="人脸识别", font=custom_font, width=10, height=3, bg="green")
    image_label.place(x=800, y=0)

    button_select = tk.Button(aly, text="选择图片", font=custom_font, width=10, height=3, bg="green", command=show)
    button_select.place(x=800, y=150)
    aly.mainloop()


def main():
    print("start")
    # 一个主界面 有三个按钮
    # Create the main window
    root.title("main")
    image = Image.open("bg_image/bg.jpg")  # 请将此处替换为您的图片路径
    image.putalpha(128)
    image = image.resize((1900, 1000))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack(fill=tk.BOTH, expand=True)
    # Create a button widget
    custom_font = font.Font(family="Helvetica", size=20)
    button_reg = tk.Button(root, text="Face Recognition", font=custom_font, width=20, height=3, bg="green", command=reg_w)
    button_cmp = tk.Button(root, text="Face Comparison", font=custom_font, width=20, height=3, bg="green", command=cmp_w)
    button_aly = tk.Button(root, text="Face Analysis", font=custom_font, width=20, height=3, bg="green", command=aly_w)

    # Pack the button into the main window
    button_reg.place(x=600, y=50)
    button_cmp.place(x=600, y=350)
    button_aly.place(x=600, y=650)
    # max
    root.state('zoomed')
    # Start the Tkinter event loop

    root.mainloop()


main()

# 选文件
# def select_file():
#     root = tk.Tk()
#
#     file_path = filedialog.askopenfilename()
#     return file_path
#
# selected_file = select_file()
# print("选择的文件路径：", selected_file)
# 功能切换
# def say_hello():
#     name = entry.get()
#     label.config(text=f"Hello, {name}!")
#
# def closeWindow():
#     root.withdraw()
#     time.sleep(3)
#     root.deiconify()
#
# # Create the main window
# root = tk.Tk()
# root.title("Tkinter Hello World")
#
# # Create a label widget
# label = tk.Label(root, text="Welcome to Tkinter!")
#
# # Pack the label into the main window
# label.pack(pady=10)
#
# # Create a button widget
# button = tk.Button(root, text="Say Hello", command=closeWindow)
#
# # Pack the button into the main window
# button.pack(pady=10)
#
# # Create an entry widget
# entry = tk.Entry(root)
#
# # Pack the entry widget into the main window
# entry.pack(pady=10)
#
# # Load an image
# image = ImageTk.PhotoImage(Image.open("image/sanjiao.jpg"))
#
# # Create a label to display the image
# image_label = tk.Label(root, image=image)
# image_label.pack(pady=10)
#
#
# # max
# root.state('zoomed')
# # Start the Tkinter event loop
# root.mainloop()
