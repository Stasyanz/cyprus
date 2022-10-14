FROM python:3.9

ADD . /app/
WORKDIR /app/
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
