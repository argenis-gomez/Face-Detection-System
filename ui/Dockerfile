FROM python:3.8.13-bullseye

WORKDIR /ui

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requeriments.txt /ui

RUN pip install -r requeriments.txt

CMD [ "streamlit", "run", "main.py"]