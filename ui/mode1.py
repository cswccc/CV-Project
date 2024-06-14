import tkinter as tk
from tkinter import END, filedialog

import cv2

from FaceRec import FaceRec
from PIL import Image, ImageTk
import os

class Ver(tk.Frame):
    def __init__(self, master, root):
        super().__init__(master)
        self.master = master
        self.root = root
        self.master.title("Recognize in Database")
        self.face_rec = FaceRec()
        self.image1_path = None
        self.image2_path = None
        self.image1_label = None
        self.image2_label = None
        self.image1_photo = None
        self.image2_photo = None
        self.create_widgets()

    def create_widgets(self):
        self.back_button = tk.Button(self, text="Back", command=self.back)
        self.back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.image1_label_text = tk.Label(self, text="Image 1:")
        self.image1_label_text.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.image1_button = tk.Button(self, text="Upload Image 1", command=self.upload_image1)
        self.image1_button.grid(row=1, column=1, padx=10, pady=10)
        self.image1_path_label = tk.Label(self, text="")
        self.image1_path_label.grid(row=2, column=1, padx=10, pady=10)

        self.image2_label_text = tk.Label(self, text="Image 2:")
        self.image2_label_text.grid(row=1, column=2, padx=10, pady=10, sticky="e")
        self.image2_button = tk.Button(self, text="Upload Image 2", command=self.upload_image2)
        self.image2_button.grid(row=1, column=3, padx=10, pady=10)
        self.image2_path_label = tk.Label(self, text="")
        self.image2_path_label.grid(row=2, column=3, padx=10, pady=10)

        self.start_button = tk.Button(self, text="Start", command=self.compare_faces)
        self.start_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        self.image1_label = tk.Label(self)
        self.image1_label.grid(row=5, column=0, padx=10, pady=10)

        self.image2_label = tk.Label(self)
        self.image2_label.grid(row=5, column=1, padx=10, pady=10)

    def back(self):
        self.master.withdraw()
        self.root.destroy()

    def upload_image1(self):
        self.image1_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.image1_path_label.config(text=self.image1_path)
        self.display_image1()

    def upload_image2(self):
        self.image2_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.image2_path_label.config(text=self.image2_path)
        self.display_image2()

    def openImage(self, type):
        self.output.delete("1.0", END)
        global img_path1, img_path2
        img_path = filedialog.askopenfilename()
        image = None
        img = None
        if img_path[-3:] == 'mp4':
            vc = cv2.VideoCapture(img_path)
            if vc.isOpened():
                rval, frame = vc.read()
                image = frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = ImageTk.PhotoImage(img)
            vc.release()
        else:
            image = cv2.imread(img_path)
            img = Image.open(img_path)
            img = ImageTk.PhotoImage(img)
        if type == 1:
            img_path1 = img_path
            self.img1 = image
            self.label_3.configure(image=img)
            self.lineEdit_3.delete(0, END)
            self.lineEdit_3.insert(0, img_path1)
        else:
            img_path2 = img_path
            self.img2 = image
            self.label_4.configure(image=img)
            self.lineEdit_4.delete(0, END)
            self.lineEdit_4.insert(0, img_path2)
    def display_image1(self):
        if self.image1_path:
            img = Image.open(self.image1_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            self.image1_photo = ImageTk.PhotoImage(img)
            self.image1_label.configure(image=self.image1_photo)

    def display_image2(self):
        if self.image2_path:
            img = Image.open(self.image2_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            self.image2_photo = ImageTk.PhotoImage(img)
            self.image2_label.configure(image=self.image2_photo)
    def compare_faces(self):
        if self.image1_path and self.image2_path:
            result = self.face_rec.verifyTwoFaces(self.image1_path, self.image2_path)
            if result[0]['verified']:
                self.result_label.config(text=f"Confidence: {result[0]['time_cost']:.2%}")
            else:
                self.result_label.config(text="Error: Unable to compare faces")
        else:
            self.result_label.config(text="Please upload two images first.")