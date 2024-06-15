import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.FaceRec import FaceRec
import utils.ImageProcess as imageProcess
import cv2
from PIL import Image, ImageTk

# 初始化 FaceRec 类
faceRec = FaceRec()

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("1200x800")

        self.face_path = None
        self.database_path = "test_images"  # 数据库路径

        self.current_face_index = 0
        self.faces = []

        self.create_widgets()

    def create_widgets(self):
        # 标题
        self.label_title = tk.Label(self.root, text="Face Recognition", font=("Arial", 24))
        self.label_title.pack(pady=20)

        # 选择图片按钮和标签
        self.btn_select_face = tk.Button(self.root, text="Select Image", command=self.select_face)
        self.btn_select_face.pack(pady=10)

        self.label_face = tk.Label(self.root, text="No image selected")
        self.label_face.pack()

        # 左右切换按钮
        self.btn_prev = tk.Button(self.root, text="Previous Face", command=self.prev_face)
        self.btn_prev.pack(pady=5)

        self.btn_next = tk.Button(self.root, text="Next Face", command=self.next_face)
        self.btn_next.pack(pady=5)

        # 大图和小图显示区域
        self.frame_images = tk.Frame(self.root)
        self.frame_images.pack()

        self.label_big_image = tk.Label(self.frame_images)
        self.label_big_image.grid(row=0, column=0, padx=20, pady=20)

        self.label_similar_faces = []
        for i in range(3):
            label = tk.Label(self.frame_images)
            label.grid(row=0, column=i + 1, padx=20, pady=20)
            self.label_similar_faces.append(label)

    def select_face(self):
        self.face_path = filedialog.askopenfilename(title="Select Image")
        if self.face_path:
            self.label_face.config(text=self.face_path)
            img = imageProcess.imageRead(self.face_path)
            self.display_image_from_array(img, self.label_big_image)
            self.process_image()

    def process_image(self):
        # 假设你有一个detectFaces方法来检测所有人脸
        faces = faceRec.detectFaces(self.face_path)
        self.faces = faces
        if faces:
            self.current_face_index = 0
            self.display_face(self.current_face_index)
        else:
            messagebox.showerror("Error", "No faces detected.")

    def display_face(self, index):
        if self.faces:
            face = self.faces[index]
            img = imageProcess.imageRead(self.face_path)
            img_with_box = imageProcess.drawRectangle(img, face['box'])
            self.display_image_from_array(img_with_box, self.label_big_image)

            # 查找相似人脸
            top_3, _ = faceRec.findSimilarFaces(face=face['image'], database_path=self.database_path)
            for i, similar_face in enumerate(top_3):
                similar_img = imageProcess.imageRead(similar_face['identity'])
                self.display_image_from_array(similar_img, self.label_similar_faces[i])

    def prev_face(self):
        if self.faces and self.current_face_index > 0:
            self.current_face_index -= 1
            self.display_face(self.current_face_index)

    def next_face(self):
        if self.faces and self.current_face_index < len(self.faces) - 1:
            self.current_face_index += 1
            self.display_face(self.current_face_index)

    def display_image_from_array(self, img_array, label):
        img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((400, 400), Image.LANCZOS)  # 调整大小以适应界面
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
