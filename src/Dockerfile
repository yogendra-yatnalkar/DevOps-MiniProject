FROM python:3.7-slim-stretch

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 66

ENTRYPOINT [ "python" ]

CMD [ "app.py"]
