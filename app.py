from flask import Flask
from waitress import serve
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!" # + os.environ['BUCKET_NAME']

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
