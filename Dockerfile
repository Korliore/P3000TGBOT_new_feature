FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    bash  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/src



CMD ["/bin/bash", "entrypoint.sh"]