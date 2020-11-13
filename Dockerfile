FROM python:3.8.6-alpine3.11

COPY requirements.txt ./
ADD ./server /server

RUN pip install --no-cache-dir -r requirements.txt

#WORKDIR /server
CMD [ "python", "/server/manage.py", "runserver", "0.0.0.0:8000" ]

#CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]