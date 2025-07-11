FROM python:3.12-alpine3.22

WORKDIR /healing_medical_record

COPY ./requirements.txt /healing_medical_record/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /healing_medical_record/requirements.txt

COPY ./app /healing_medical_record/app
