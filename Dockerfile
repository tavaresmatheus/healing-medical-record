FROM python:3.12-slim-bookworm

WORKDIR /healing_medical_record

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /healing_medical_record/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /healing_medical_record/requirements.txt

COPY ./app /healing_medical_record/app
