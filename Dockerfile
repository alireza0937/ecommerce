FROM python:alpine3.19
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY req.txt .
RUN pip install --upgrade pip \
    && pip install -r req.txt
COPY . .
