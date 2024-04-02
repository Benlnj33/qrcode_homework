FROM python:3.11

WORKDIR /Users/benlnj33/Desktop/IS601/projects/qrcode_homework

COPY qrcode_generator.py .

RUN pip install qrcode[pil] qrcode-terminal

CMD ["python", "qrcode_generator.py"]
