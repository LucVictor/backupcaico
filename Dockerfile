FROM python:3.14-rc-alpine3.21
COPY ./ /app
WORKDIR /app
RUN ls -a
RUN apk update && apk add mysql mysql-client
RUN mkdir backups
RUN pip3 install -r requirements.txt
CMD [ "python3", "script.py"]