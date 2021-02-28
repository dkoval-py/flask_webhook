FROM python:3.7-alpine

ADD requirements.txt /
RUN pip install --no-cache -r /requirements.txt

WORKDIR /webhook
COPY application/ /webhook
CMD [ "python", "./webhook.py" ]
