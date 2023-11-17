# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ARG DEMO_SECRET
ENV DEMO_SECRET=$DEMO_SECRET

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]