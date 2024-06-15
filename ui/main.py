import sys
import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, font
from mode1 import Cmp
from utils.FaceRec import FaceRec
from utils.ImageProcess import *
import cv2 as cv
from aly_ui import aly_w
from face_recognition_ui import FaceRecognitionApp  # 确保正确导入



# .withdraw()  隐藏窗口
# .deiconify() 显示窗口


root = tk.Tk()
reg = tk.Toplevel()

reg.title("ver")
reg.withdraw()
cmp = tk.Toplevel()
cmp.title("cmp")
cmp.withdraw()
aly = tk.Toplevel()
aly.title("aly")
aly.withdraw()

#for aly
image_show = None
info_show = ""




#关闭设置
def on_closing():
    # 在这里可以添加一些清理操作，例如保存数据等
    sys.exit()
root.protocol("WM_DELETE_WINDOW", on_closing)
reg.protocol("WM_DELETE_WINDOW", on_closing)
cmp.protocol("WM_DELETE_WINDOW", on_closing)
aly.protocol("WM_DELETE_WINDOW", on_closing)





def back(win,image_label,info_label):
    image_label.destroy()
    info_label.destroy()

    root.deiconify()
    root.state('zoomed')
    win.withdraw()





def reg_w():
    print("reg")
    root.withdraw()
    reg.deiconify()
    reg.state('zoomed')
    app = FaceRecognitionApp(reg)  # 创建 FaceRecognitionApp 实例
    reg.mainloop()


def cmp_w():
    for widget in cmp.winfo_children():
        widget.destroy()
    print("cmp")
    root.withdraw()
    cmp.deiconify()
    cmp.state('zoomed')
    recognize_in_db = Cmp(cmp, root)
    recognize_in_db.pack(fill="both", expand=True)
    cmp.mainloop()




def main():
    print("start")
    # 一个主界面 有三个按钮
    # Create the main window
    root.title("main")
    image = Image.open("bg.jpg")  # 请将此处替换为您的图片路径
    image.putalpha(128)
    image = image.resize((1900, 1000))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack(fill=tk.BOTH, expand=True)
    # Create a button widget
    custom_font = font.Font(family="Helvetica", size=20)
    button_reg = tk.Button(root, text="Face Recognition", font=custom_font, width=20, height=3, bg="green", command=reg_w)
    button_cmp = tk.Button(root, text="Face Comparison", font=custom_font, width=20, height=3, bg="green", command=cmp_w)
    button_aly = tk.Button(root, text="Face Analysis", font=custom_font, width=20, height=3, bg="green",command=lambda:aly_w(aly, root, back))
    # Pack the button into the main window
    button_reg.place(x=700, y=50)
    button_cmp.place(x=700, y=350)
    button_aly.place(x=700, y=650)
    # max
    root.state('zoomed')
    # Start the Tkinter event loop

    root.mainloop()


if __name__ == "__main__":
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
