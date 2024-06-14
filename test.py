from FaceRec import FaceRec


faceRec = FaceRec("Facenet512")

face1 = "333.jpg"
face2 = "test_images/2.png"

# print(faceRec.analyzeFace())

print(faceRec.findSimilarFaces(face_path=face1, database_path="test_images"))