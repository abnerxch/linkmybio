FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "bio.py"]
ENTRYPOINT flask run -h 0.0.0.0 -p 5000