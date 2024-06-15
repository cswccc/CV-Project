import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import utils.ImageProcess as imageProcess
from utils.FaceRec import FaceRec
from deepface import DeepFace
from tkinter import ttk

# 初始化 FaceRec 类
faceRec = FaceRec(selected_model="VGG-Face", detect_backend="opencv")

class FaceRecognitionApp:
    def __init__(self, root, back_callback):
        self.top_3 = []
        self.source_box = []
        self.tot_faces = 0

        self.root = root
        self.back_callback = back_callback
        self.root.title("Face Recognition")
        self.root.geometry("1200x800")

        # 设置背景图片
        self.background_image = Image.open("bg.jpg")
        self.background_image = self.background_image.resize((1200, 800), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.face_path = None
        self.database_path = "C:\\Users\\ZCR\\Desktop\\VGG-cut\\VGG-cut\\n001146"  # 数据库路径

        self.current_face_index = 0
        self.faces = []

        self.create_widgets()

    def create_widgets(self):
        # 标题
        self.label_title = tk.Label(self.root, text="Face Recognition", font=("Arial", 24, "bold"), bg="white")
        self.label_title.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        # 选择图片按钮和标签
        self.btn_select_face = ttk.Button(self.root, text="Select Image", command=self.select_face)
        self.btn_select_face.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.label_face = tk.Label(self.root, text="No image selected", font=("Arial", 12), bg="white")
        self.label_face.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # 左右切换按钮
        self.btn_prev = ttk.Button(self.root, text="Previous Face", command=self.prev_face)
        self.btn_prev.place(relx=0.4, rely=0.9, anchor=tk.CENTER)

        self.btn_next = ttk.Button(self.root, text="Next Face", command=self.next_face)
        self.btn_next.place(relx=0.6, rely=0.9, anchor=tk.CENTER)

        # 返回按钮
        self.btn_back = ttk.Button(self.root, text="Back", command=self.back)
        self.btn_back.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

        # 大图和小图显示区域
        self.label_big_image = tk.Label(self.root, bg="white")
        self.label_big_image.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        self.label_similar_faces = []
        for i in range(3):
            label = tk.Label(self.root, bg="white")
            label.place(relx=0.7, rely=0.3 + i * 0.2, anchor=tk.CENTER)
            self.label_similar_faces.append(label)

    def select_face(self):
        self.face_path = filedialog.askopenfilename(title="Select Image")
        if self.face_path:
            self.label_face.config(text=self.face_path)
            self.process_image()
            self.get_matched_face()
            self.display_face(self.current_face_index)

    def process_image(self):
        faces = self.detect_faces(self.face_path)
        self.faces = faces
        print("Detected faces:", self.faces)  # 添加调试输出
        if self.faces:
            self.current_face_index = 0
        else:
            messagebox.showerror("Error", "No faces detected.")

    def detect_faces(self, img_path):
        try:
            img = cv2.imread(img_path)
            detections = DeepFace.extract_faces(img, enforce_detection=False)
            faces = [{'box': detection['facial_area'], 'image': detection['face']} for detection in detections]
            print("Faces detected:", faces)  # 添加调试输出
            return faces
        except Exception as e:
            print("Error detecting faces:", e)  # 添加错误输出
            return []

    def get_matched_face(self):
        img = imageProcess.imageRead(self.face_path)
        self.top_3 = []
        self.source_box = []
        self.tot_faces = 0

        # 查找相似人脸
        try:
            top_3, source_box = faceRec.findSimilarFaces(face=img, database_path=self.database_path)
        except Exception as e:
            print("Error finding similar faces:", e)
            return

        self.top_3 = top_3
        self.source_box = source_box
        self.tot_faces = len(top_3)

    def display_face(self, idx):
        source_img = imageProcess.imageRead(self.face_path)
        source_img = imageProcess.drawRectangle(source_img, self.source_box[idx])

        top_3_image = []

        for matched in self.top_3[idx]:
            matched_img = imageProcess.imageRead(matched['identity'])
            matched_img = imageProcess.drawRectangle(matched_img, matched['box'])
            top_3_image.append(matched_img)

        # 调整左侧大图的大小，使其宽度等于右侧三个小图宽度之和
        self.display_image_from_array(source_img, self.label_big_image, (400, 400))

        for i in range(len(top_3_image)):
            self.display_image_from_array(top_3_image[i], self.label_similar_faces[i], (200, 200))

    def prev_face(self):
        if self.tot_faces != 0 and self.current_face_index > 0:
            self.current_face_index -= 1
            self.display_face(self.current_face_index)

    def next_face(self):
        if self.tot_faces != 0 and self.current_face_index < self.tot_faces - 1:
            self.current_face_index += 1
            self.display_face(self.current_face_index)

    def display_image_from_array(self, img_array, label, size):
        img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize(size, Image.LANCZOS)  # 调整大小以适应界面
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img

    def back(self):
        self.back_callback(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    def back_callback(win):
        win.withdraw()
        root.deiconify()
        root.state('zoomed')
    app = FaceRecognitionApp(root, back_callback)
    root.mainloop()
