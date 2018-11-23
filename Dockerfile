FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add libssl1.0 gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev libffi-dev openssl-dev && \
    rm -rf /var/cache/apk/*

COPY proxy.py ./

ENV FLASK_APP proxy.py
ENV UNAME Administrator
ENV PASSWORD pw01

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
