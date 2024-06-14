from deepface import DeepFace
import cv2 as cv
from utils.ImageProcess import *

class FaceRec:
    """
    Face recognition with DeepFace.
    Args:
        selected_model (str): The selected face recognition model.
        detect_backend (str): The selected detect backend.
    """
    def __init__(self, selected_model="Facenet512", detect_backend='opencv'):
        self.models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepID", "ArcFace"]
        self.backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'fastmtcnn', 'retinaface',  'mediapipe', 'yolov8', 'yunet', 'centerface']

        self.selected_model = selected_model
        self.detect_backend = detect_backend

    def verifyTwoFaces(self, face1, face2):
        """
        Compare the two imgs to see if they are the same person.
        Args:
            face1 (np.ndarray): The first face.
            face2 (np.ndarray): The second face.
        Returns:
            ret (list): The verify result for the two face, includes 'verified', 'face1_box', 'time_cost'.
        """
        result = DeepFace.verify(face1, face2, model_name=self.selected_model, detector_backend=self.detect_backend)

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
    
    def findSimilarFaces(self, face, database_path):
        """
        Select the most similar three face imgs from the database.
        Args:
            face (np.ndarray): The input face.
            database_path (str): Path of the database.
        Returns:
            top_3 (list): The first three similar image information, including 'identity' and 'box'.
            source_box (list):  Facial position information of the input image.
        """
        results = DeepFace.find(face, db_path=database_path, model_name=self.selected_model, detector_backend=self.detect_backend)

        top_3 = []
        source_box = []
        for result in results:
            source_box.append([result.source_x[0], result.source_y[0], result.source_w[0], result.source_h[0]])
            identity = result.identity; target_x = result.target_x; target_y = result.target_y; target_w = result.target_w; target_h = result.target_h
            now_top_3 = []
            
            for i in range(min(len(identity), 3)):
                now_top_3.append({
                    'identity': identity[i],
                    'box': [target_x[i], target_y[i], target_w[i], target_h[i]]
                })

            top_3.append(now_top_3)

        return top_3, source_box
    
    def analyzeFace(self, face, actions=['emotion', 'age', 'gender']):
        """
        Analyzing facial information in images.
        Args:
            face (np.ndarray): The input face.
            actions (list): Properties that need to be analyzed.
        Returns:
            ret (list): Facial detection information.
        """
        results = DeepFace.analyze(face, actions=actions, detector_backend=self.detect_backend)

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
    
    def cameraCall(self, database_path=None):
        """
        DeepFace real-time face detection.
        """
        DeepFace.stream(db_path = database_path, detector_backend=self.detect_backend)
