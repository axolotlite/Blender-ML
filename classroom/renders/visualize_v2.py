

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
        cv2.circle(img,(int(keypoint[0]),int(keypoint[1])),1,(255, 0, 0),5)

    cv2.rectangle(img,(int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,0,255),1)
    

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



