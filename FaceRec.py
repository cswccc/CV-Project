from deepface import DeepFace
import pandas as pd


class FaceRec:
    def __init__(self, selected_model="Facenet512"):
        self.models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepID", "ArcFace"]

        self.selected_model = selected_model

    def verifyTwoFaces(self, face1, face2, selected_model="Facenet512"):
        if selected_model is None:
            selected_model = self.selected_model
            
        result = DeepFace.verify(face1, face2, model_name=selected_model)


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
    
    def findSimilarFaces(self, face, database_path, selected_model="Facenet512"):
        if selected_model is None:
            selected_model = self.selected_model

        result = DeepFace.find(face, db_path=database_path, model_name=selected_model)

        identity = result[0].identity; target_x = result[0].target_x; target_y = result[0].target_y; target_w = result[0].target_w; target_h = result[0].target_h

        top_3 = []
        source_box = [result[0].source_x[0], result[0].source_y[0], result[0].source_w[0], result[0].source_h[0]]

        print(result)
        print('---')

        for i in range(min(len(identity), 3)):
            top_3.append({
                'identity': identity[i],
                'box': [target_x[i], target_y[i], target_w[i], target_h[i]]
            })

        return top_3, source_box
    
    def analyzeFace(self, face, actions=['emotion', 'age', 'gender']):
        results = DeepFace.analyze(face, actions=actions)


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
