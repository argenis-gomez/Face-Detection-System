import torch
import sys

def get_yolov5():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./dependencies/weights/best.pt', force_reload=True)
    model.conf = 0.5
    return model
