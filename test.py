from FaceRec import FaceRec
from ImageProcess import *
import cv2 as cv

faceRec = FaceRec("ArcFace")

face1 = "test.png"
face2 = "test_images/2.png"



print(faceRec.verifyTwoFaces(face1_path=face1, face2_path=face2))
print('****************************************************************************************')


print(faceRec.findSimilarFaces(face_path=face1, database_path="test_images"))
print('****************************************************************************************')


res = faceRec.analyzeFace(face_path=face1)
print(res)
print('****************************************************************************************')

img = imageRead(face1)
out = img.copy()
for result in res:
    info = result['emotion'] + ' ' + result['gender'] + ' ' + str(result['age'])

    out = drawRectangle(out, res[0]['box'], additionInfo=info)

cv.imshow('result', out)
cv.waitKey(0)