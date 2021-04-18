FROM python:3.8.7-alpine3.11

EXPOSE 3000

COPY . /pythonapp
WORKDIR /pythonapp

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "src/app.py"]

