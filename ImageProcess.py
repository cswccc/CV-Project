import cv2 as cv
import numpy

def imageRead(img_path):
    img = cv.imread(img_path)

    return img

def imageResize(img, new_size):
    img = cv.resize(img, new_size)

    return img

def drawRectangle(img, boxes, additionInfo=None, box_color=(0, 0, 255), fps=None, text_color=(0, 255, 0)):
    process_img = img.copy()

    for box in boxes:
        x = box[0]; y = box[1]; w = box[2]; h = box[3]
        
        process_img = cv.rectangle(process_img, (x, y), (x + w, y + h), box_color, 1)

        if additionInfo is not None:
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            text_size, baseline = cv.getTextSize(additionInfo, cv.FONT_HERSHEY_DUPLEX, 0.4, 1)
            text_x = center_x - int(text_size[0] / 2)
            text_y = center_y - int(text_size[1] / 2)

            process_img = cv.putText(process_img, additionInfo,(text_x, text_y),cv.FONT_HERSHEY_DUPLEX,0.4,(0,0,255),1)
    
    if fps is not None:
        cv.putText(process_img, 'FPS: {:.2f}'.format(fps), (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, text_color)

    return process_img