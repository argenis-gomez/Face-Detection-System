from unittest import result
from pydantic import BaseModel
from typing import List

class Faces(BaseModel):
    name: str
    image_b64: str

class YoloResuls(BaseModel):
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    name: str


class FaceResponse(BaseModel):
    result: List[YoloResuls]