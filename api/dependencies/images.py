from PIL import Image
import io
import base64

def get_image_from_bytes(b64_image):

    b64_image = bytes(b64_image, 'utf-8')
    input_image = Image.open(io.BytesIO(base64.decodebytes(b64_image)))

    resized_image = input_image.resize((512, 512))
    return resized_image