from FaceRec import FaceRec


faceRec = FaceRec("Facenet512")

face1 = "test.png"

# print(faceRec.analyzeFace())

print(faceRec.findSimilarFaces(face_path=face1, database_path="test_images"))