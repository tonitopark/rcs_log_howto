FROM python:3.7.3

WORKDIR /logger

COPY req.txt req.txt

RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY . /logger
