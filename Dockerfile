FROM  python:3.11-rc-alpine

# We want proper container logging
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add bash inotify-tools

# Install requirements
COPY requirements.txt /etc/requirements.txt
RUN pip install -r /etc/requirements.txt

# Set working directory to project
WORKDIR /app
COPY . /app
