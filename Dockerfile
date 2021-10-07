# FROM ubuntu:20.04

FROM python:3

ADD main.py /

CMD [ "python", "./main.py" ]

