from FaceRec import FaceRec
from ImageProcess import *
import cv2 as cv

faceRec = FaceRec("ArcFace")

face1 = "test.png"
face2 = "test_images/2.png"

face1 = imageRead(face1)
face2 = imageRead(face2)


print(faceRec.verifyTwoFaces(face1=face1, face2=face2))
print('****************************************************************************************')


print(faceRec.findSimilarFaces(face=face1, database_path="test_images"))
print('****************************************************************************************')


res = faceRec.analyzeFace(face=face1)
print(res)
print('****************************************************************************************')

img = imageRead("test.png")
out = img.copy()
for result in res:
    info = result['emotion'] + ' ' + result['gender'] + ' ' + str(result['age'])

    out = drawRectangle(out, res[0]['box'], additionInfo=info)

cv.imshow('result', out)
cv.waitKey(0)