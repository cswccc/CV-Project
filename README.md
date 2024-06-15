# CV-Project



### Class FaceRec

#### verifyTwoFaces

**Params:**

face1: 第一个人脸照片

face2: 第二个人脸照片

selected_model(Optional): 跑DeepFace选择的model, 默认是"Facenet512"

**Return:**

ret: 两个人脸比较的信息, 包含verified(是否是一个人), face1_box(第一个人脸的位置), face2_box(第二个人脸的位置), time_cost(消耗的时间, 没太大用)

Example:

```python
res = faceRec.verifyTwoFaces(face1=face1, face2=face2)

print(res)
-----------------------------------------------------------------------------------------
Output:
[{'verified': True, 'face1_box': [158, 124, 262, 262], 'face2_box': [158, 124, 262, 262], 'time_cost': 5.39}]
*****************************************************************************************

print(res[0]['verified'])
-----------------------------------------------------------------------------------------
Output:
True
*****************************************************************************************
```



#### findSimilarFaces

**Params:**

face: 要比较的人脸照片

database_path: 对比数据库路径

selected_model: 选择的模型

**Return:**

top_3: 前三相似的人脸照片信息, 包括identity(照片的路径信息), box(人脸框)

source_box: 比较照片的人脸框

Example:

```python
top_3, source_box = faceRec.findSimilarFaces(face=face1, database_path="test_images")

print(top_3, source_box)
-----------------------------------------------------------------------------------------
Output:
[{'identity': '../VGG-cut\\n000001\\0001_01.jpg', 'box': [40, 66, 103, 103]}, {'identity': '../VGG-cut\\n000001\\0023_01.jpg', 'box': [76, 27, 182, 182]}, {'identity': '../VGG-cut\\n000001\\0002_01.jpg', 'box': [88, 76, 300, 300]}]
[40, 66, 103, 103]
****************************************************************************************
```



#### analyzeFace

**Params:**

face: 分析人脸路径
actions: 要分析得到的信息, 默认是['emotion', 'age', 'gender']

**Return:**

ret: 人脸的信息, 包括emotion, gender, age, box(人脸框)

Example:

```python
res = faceRec.analyzeFace(face=face1)
print(res)
-----------------------------------------------------------------------------------------
Output:
[{'emotion': 'happy', 'gender': 'Man', 'age': 27, 'box': [158, 124, 262, 262]}]
****************************************************************************************
```



### ImageProcess

#### imageRead(img_path) 

图片读取



#### imageResize(img) 

图片size变换



#### drawRectangle(img, box, additionInfo=None, box_color=(0, 0, 255), fps=None, text_color=(0, 255, 0))

给图片框人脸

**Params:**

img: 要处理的图片

box: 框的位置信息

additionInfo: 附着文字, 可以有也可以没有, 会在调用analyzeFace之后添加

box_color: 框的颜色, 随便设置, 可以不传

fps: 帧率信息, 可能会在视频中用到

text_color: 附着文字的颜色