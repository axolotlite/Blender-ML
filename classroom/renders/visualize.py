

from PIL import Image
import cv2
import numpy as np

import json

with open('labels.json') as data_file:
    data = json.load(data_file)



for object in data:
    img = object['image']
    bbox = object['bbox']
    keypoints = object['keypoints']
    print(keypoints)
    image = cv2.imread(img)
    height, width, channels = image.shape
    print(height, width)
    img = image
    for keypoint in keypoints:
        print(keypoint)
        xk1 = keypoint[0] * width
        yk1 = height - keypoint[1] * height

        cv2.circle(img,(int(xk1),int(yk1)),1,(255, 0, 0),5)
    x1 = bbox[0] * width
    y1 = height - bbox[1] * height
    x2 = bbox[2] * width
    y2 = height - bbox[3] * height
    cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)
    

#    for shape in obj:
#        shape = obj[shape]
#        x1 = shape['x1'] * width
#        x2 = shape['x2'] * width

#        y1 = shape['y1'] * height 
#        y2 = shape['y2'] * height 
#        y1 = height - y1
#        y2 = height - y2
#        cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)

    cv2.imshow('image',img)
    cv2.waitKey(0)



