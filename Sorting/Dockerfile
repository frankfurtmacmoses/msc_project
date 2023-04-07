FROM python:3
RUN apt-get update && \
apt-get install -y curl && \
rm -rf varlib/apt/lists/*
WORKDIR /app
COPY sorting.py /app/
ENTRYPOINT ["python", "sorting.py"]