FROM python:3
RUN apt-get update && \
apt-get install -y curl && \
rm -rf varlib/apt/lists/*
WORKDIR /app
COPY handler.py /app/
COPY requirements.txt   .
RUN pip install -r requirements.txt
RUN python3 -m textblob.download_corpora lite
ENTRYPOINT ["python", "handler.py"]

 