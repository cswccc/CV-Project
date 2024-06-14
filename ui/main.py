import time
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

from ui.mode1 import Ver

#.withdraw()  隐藏窗口
#.deiconify() 显示窗口

root = tk.Tk()
reg = tk.Tk()

reg.title("ver")
reg.withdraw()
cmp = tk.Tk()
cmp.title("cmp")
cmp.withdraw()
aly = tk.Tk()
aly.title("aly")
aly.withdraw()
def back(win):
    root.deiconify()
    root.state('zoomed')
    win.withdraw()

def reg_w():
    print("reg")
    root.withdraw()
    reg.deiconify()
    reg.state('zoomed')

    recognize_in_db = Ver(reg, root)
    recognize_in_db.pack(fill="both", expand=True)

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
    # Start the Tkinter event loop
    button_b = tk.Button(aly, text="back", command=lambda: back(aly))
    button_b.pack(pady=10)
    aly.mainloop()

def main():
    print("start")
    # 一个主界面 有三个按钮

    # Create the main window
    root.title("main")
    # Create a button widget
    button_reg = tk.Button(root, text="reg", command=reg_w)
    button_cmp = tk.Button(root, text="cmp", command=cmp_w)
    button_aly = tk.Button(root, text="aly", command=aly_w)

    # Pack the button into the main window
    button_reg.pack(pady=10)
    button_cmp.pack(pady=10)
    button_aly.pack(pady=10)
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
