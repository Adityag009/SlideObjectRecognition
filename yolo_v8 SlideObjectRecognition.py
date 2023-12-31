# -*- coding: utf-8 -*-
"""YOLO V8

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157_ZgER2BxcJEbTESiDsQxmzqsKs4NYj
"""

!nvidia-smi

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# Change directory to your project folder
# %cd /content/drive/MyDrive/YOLO V8/Revent2.ai.v1i.yolov8



!pip install ultralytics==8.0.28

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/YOLO V8/Revent2.ai.v1i.yolov8

!yolo task=segment mode=train model=yolov8s-seg.pt data=data.yaml epochs=25 imgsz=640

!ls runs/segment/train2

Image(filename='runs/segment/train2/confusion_matrix.png', width=600)

Image(filename='runs/segment/train2/results.png', width=600)

Image(filename='runs/segment/train2/val_batch0_pred.jpg', width=600)

!yolo task=detect mode=val model=runs/segment/train2/weights/best.pt data=data.yaml

!yolo task=detect mode=predict model=runs/segment/train2/weights/best.pt conf=0.25 source=test/images

!yolo task=detect mode=predict model=runs/segment/train2/weights/best.pt conf=0.25 source=pred2



import glob
from IPython.display import Image, display

for image_path in glob.glob('runs/detect/pred2/*.jpg')[:3]:
      display(Image(filename=image_path, width=600))
      print("\n")



