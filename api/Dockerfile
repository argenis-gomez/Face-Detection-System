FROM python:3.8.13-bullseye

WORKDIR /api

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requeriments.txt /api

RUN pip install -r requeriments.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80",  "--reload" ]