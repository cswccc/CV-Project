from deepface import DeepFace
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
import cv2
import numpy as np


class FaceRec:
    def __init__(self, selected_model=None):
        self.models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepID", "ArcFace"]
        if selected_model is None:
            self.selected_model = "Facenet512"

        self.selected_model = selected_model

    def verifyTwoFaces(self, face1_path, face2_path, selected_model=None):
        if selected_model is None:
            selected_model = self.selected_model
            
        result = DeepFace.verify(img1_path=face1_path, img2_path=face2_path, model_name=selected_model)


        ret = []
        f1_region = result['facial_areas']['img1']
        f2_region = result['facial_areas']['img2']
        ret.append({
            'verified': result['verified'],
            'face1_box': [f1_region['x'], f1_region['y'], f1_region['w'], f1_region['h']],
            'face2_box': [f2_region['x'], f2_region['y'], f2_region['w'], f2_region['h']],
            'time_cost': result['time']
        })

        return ret
    
    def findSimilarFaces(self, face_path, database_path, selected_model=None):
        if selected_model is None:
            selected_model = self.selected_model

        result = DeepFace.find(img_path=face_path, db_path=database_path, model_name=selected_model)

        return result
    
    def analyzeFace(self, face_path, actions=['emotion', 'age', 'gender']):
        results = DeepFace.analyze(img_path=face_path, actions=actions)


        ret = []
        for result in results:
            region = result['region']

            ret.append({
                'emotion': result['dominant_emotion'],
                'gender': result['dominant_gender'],
                'age': result['age'],
                'box': [region['x'], region['y'], region['w'], region['h']]
            })

        return ret
