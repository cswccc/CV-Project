import tkinter as tk
from tkinter import END, filedialog
from utils.FaceRec import FaceRec
from PIL import Image, ImageTk
from utils.ImageProcess import *
class Cmp(tk.Frame):
    def __init__(self, master, root):
        super().__init__(master)
        self.master = master
        self.root = root
        self.face_rec = FaceRec()
        self.image1_path = None
        self.image2_path = None
        self.image1_label = None
        self.image2_label = None
        self.image1_photo = None
        self.image2_photo = None
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Face Comparison")
        self.master.configure(bg="#F0F0F0")

        image = Image.open("bg.jpg")
        image.putalpha(128)
        image = image.resize((1900, 1000))
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(self, text="Face Comparison", font=("Arial", 30, "bold"), fg="#FFA500", bg="#90EE90", padx=20, pady=10)
        title_label.place(x=780, y=40, anchor="center")

        self.back_button = tk.Button(self, text="Back", font=("Arial", 16), fg="white", bg="#4CAF50",
                                     command=lambda: self.back())
        self.back_button.place(x=20, y=20)

        self.image1_label_text = tk.Label(self, text="Image 1:", font=("Arial", 18), fg="#333333", bg="#90EE90")
        self.image1_label_text.place(x=300, y=80, anchor="center")
        self.image1_button = tk.Button(self, text="Upload Image 1", font=("Arial", 14), fg="white", bg="#007BFF",
                                       command=self.upload_image1)
        self.image1_button.place(x=450, y=80, anchor="center")
        self.image1_path_label = tk.Label(self, text="path", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
        self.image1_path_label.place(x=450, y=120, anchor="center")

        self.image2_label_text = tk.Label(self, text="Image 2:", font=("Arial", 18), fg="#333333", bg="#90EE90")
        self.image2_label_text.place(x=1050, y=80, anchor="center")
        self.image2_button = tk.Button(self, text="Upload Image 2", font=("Arial", 14), fg="white", bg="#007BFF",
                                       command=self.upload_image2)
        self.image2_button.place(x=1200, y=80, anchor="center")
        self.image2_path_label = tk.Label(self, text="path", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
        self.image2_path_label.place(x=1200, y=120, anchor="center")

        self.start_button = tk.Button(self, text="Start", font=("Arial", 20, "bold"), fg="white", bg="#FFA500",
                                      command=self.compare_faces)
        self.start_button.place(x=780, y=150, anchor="center")

        self.result_label = tk.Label(self, text="", font=("Arial", 20), fg="#DC143C", bg="#90EE90")
        self.result_label.place(x=825, y=750, anchor="center")

        self.image1_display = tk.Label(self, text="Input1", font=("Arial", 18, "bold"), fg="#333333", bg="#90EE90")
        self.image1_display.place(x=450, y=200, anchor="center")
        self.image1_label = tk.Label(self)
        self.image1_label.place(x=450, y=480, anchor="center")
        self.image2_display = tk.Label(self, text="Input2", font=("Arial", 18, "bold"), fg="#333333", bg="#90EE90")
        self.image2_display.place(x=1200, y=200, anchor="center")
        self.image2_label = tk.Label(self)
        self.image2_label.place(x=1200, y=480, anchor="center")
    def back(self):
        self.master.withdraw()
        self.root.deiconify()
    def upload_image1(self):
        self.image1_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.image1_path_label.config(text=self.image1_path)
        self.display_image1()
    def upload_image2(self):
        self.image2_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.image2_path_label.config(text=self.image2_path)
        self.display_image2()
    def display_image1(self):
        if self.image1_path:
            img = Image.open(self.image1_path)
            img = img.resize((400, 400), Image.ANTIALIAS)
            self.image1_photo = ImageTk.PhotoImage(img)
            self.image1_label.configure(image=self.image1_photo)
    def display_image2(self):
        if self.image2_path:
            img = Image.open(self.image2_path)
            img = img.resize((400, 400), Image.ANTIALIAS)
            self.image2_photo = ImageTk.PhotoImage(img)
            self.image2_label.configure(image=self.image2_photo)
    def compare_faces(self):
        if self.image1_path and self.image2_path:
            try:
                img1 = imageRead(self.image1_path)
                img2 = imageRead(self.image2_path)
                result = self.face_rec.verifyTwoFaces(img1, img2)
                if len(result) == 0:
                    self.result_label.config(text="No face detected in one of the images.")
                    return
                img1 = drawRectangle(img1, result[0]['face1_box'])
                img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
                img1 = Image.fromarray(img1)
                img1 = img1.resize((400, 400), Image.ANTIALIAS)
                self.image1_photo = ImageTk.PhotoImage(img1)
                self.image1_label.configure(image=self.image1_photo)
                img2 = drawRectangle(img2, result[0]['face2_box'])
                img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
                img2 = Image.fromarray(img2)
                img2 = img2.resize((400, 400), Image.ANTIALIAS)
                self.image2_photo = ImageTk.PhotoImage(img2)
                self.image2_label.configure(image=self.image2_photo)
                if result[0]['verified']:
                    self.result_label.config(text="They are the Same person.")
                else:
                    self.result_label.config(text="They are not the Same person.")
            except Exception as e:
                self.result_label.config(text="Error occurred while comparing faces: {}".format(str(e)))
        else:
            self.result_label.config(text="Please upload two images first.")
