import base64
import json
import torch

from fastapi import APIRouter, File

from schemas.faces import Faces, FaceResponse
from dependencies.load_models import get_yolov5
from dependencies.images import get_image_from_bytes

faces = APIRouter()

models = {
    'yolov5': get_yolov5()
}

@faces.post('/faces/v1', response_model=FaceResponse, tags=["face_detection"])
async def predict_faces(body: Faces):

    body = dict(body)

    image = get_image_from_bytes(body['image_b64'])

    results = models['yolov5'](image)
    
    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    return {"result": detect_res}


    