from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
import cv2
import numpy as np


class FaceRec:
    def __init__(self, selected_model):
        self.models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepID", "ArcFace"]
        self.selected_model = selected_model

    def verifyTwoFaces(self, face1_path, face2_path, selected_model=None):
        if selected_model is None:
            selected_model = self.selected_model
            
        result = DeepFace.verify(img1_path=face1_path, img2_path=face2_path, model_name=selected_model)

        return result
    
    def findSimilarFaces(self, face_path, database_path, selected_model=None):
        if selected_model is None:
            selected_model = self.selected_model

        result = DeepFace.find(img_path=face_path, db_path=database_path, model_name=selected_model)

        return result
    
    def analyzeFace(self, face_path, actions):
        result = DeepFace.analyze(img_path=face_path, actions=actions)

        return result
