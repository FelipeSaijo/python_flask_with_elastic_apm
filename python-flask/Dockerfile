FROM python:3.11.4-alpine3.18

RUN apk -i update \
    && apk -i upgrade

RUN apk -i add \
    nginx \
    python3-dev \
    libpq-dev

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY app .

EXPOSE 5000
CMD [ "python", "app.py" ]