from utils.FaceRec import FaceRec
from utils.ImageProcess import *
import cv2 as cv

faceRec = FaceRec("ArcFace")

face1 = "test_images/8.png"
face1 = imageRead(face1)

print(face1.shape)

face2 = "test_images/2.png"
face2 = imageRead(face2)


# print(faceRec.verifyTwoFaces(face1=face1, face2=face2))
# print('****************************************************************************************')




# top_3, source_box = faceRec.findSimilarFaces(face=face1, database_path="test_images")
# # print(top_3, source_box)
# for i in range(len(source_box)):
#     now_top_3 = top_3[i]
#     now_box = source_box[i]
#     print(now_top_3)
#     print(now_box)
#     print('------0------')
# print('****************************************************************************************')




res = faceRec.analyzeFace(face=face1)
print(res)
img = imageRead("test.png")
out = face1.copy()
for result in res:
    info = result['emotion'] + ' ' + result['gender'] + ' ' + str(result['age'])

    out = drawRectangle(out, result['box'], additionInfo=info)

cv.imshow('result', out)
cv.waitKey(0)
print('****************************************************************************************')

# faceRec.cameraCall(database_path="test_images")