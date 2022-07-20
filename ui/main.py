import streamlit as st
import base64
import json
import requests
import cv2
import numpy as np


def plot_prediction(image, predictions):
    image = np.asarray(bytearray(image), dtype=np.uint8)
    image = cv2.imdecode(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (512, 512))

    for pred in predictions['result']:
        cv2.rectangle(image, (int(pred['xmin']), int(pred['ymin'])), (int(pred['xmax']), int(pred['ymax'])), (255, 0, 0), 1)
        cv2.putText(image, f"{pred['name']}: {pred['confidence']: .2f}", (int(pred['xmin']), int(pred['ymin'])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    st.image(image, width=512)


def main():

    st.title('Detector de Caras')

    uploaded_file = st.file_uploader(label="Selecciona una imagen con caras:",
                                     type=["png", "jpeg", "jpg"])

    if not uploaded_file:
        st.warning("Por favor subir una imagen.")
        st.stop()
    else:
        uploaded_image = uploaded_file.read()
        st.image(uploaded_image, width=512)

        if st.button('Identificar'):

            body_dict = {
                "name": uploaded_file.name,
                "image_b64": base64.b64encode(uploaded_image).decode('utf-8')
            }
            
            
            json_body = json.dumps(body_dict)
            
            response = requests.post('http://api/faces/v1',
                data=json_body,
                headers={'Content-Type': 'application/json'}
                 )

            if response.status_code == 200:
                plot_prediction(uploaded_image, response.json())



if __name__ == '__main__':

    main()