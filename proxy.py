import requests
import os
from requests_ntlm import HttpNtlmAuth
from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    username = os.getenv('UNAME')
    password = os.getenv('PASSWORD')
    base_url = os.getenv('URL')

    qs = request.query_string.decode('utf-8')

    url = base_url + '/' + path
    if qs:
        url += '?' + qs

    app.logger.info(url)

    r = requests.get(url, auth=HttpNtlmAuth(username, password))

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in r.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(r.content, r.status_code, headers)
    return response
