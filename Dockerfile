FROM python:3.9.0-alpine

RUN mkdir -p /home/data
RUN mkdir -p /home/output

WORKDIR /home/src

COPY hw2.py .
#COPY testing.txt ../data
#COPY testing2.txt ../data

CMD ["python", "hw2.py"]