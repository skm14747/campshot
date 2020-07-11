# Base image
FROM python:3.7-slim

# Install vital elements
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    gdal-bin \
    libcurl4-openssl-dev \
    libssl-dev \
    python3-dev \
    && pip install --upgrade pip \
    && pip install gunicorn

# Construct the cockpit
RUN mkdir /code
WORKDIR /code

# Install app's vital elements
COPY requirements.txt .
RUN pip install -r requirements.txt
