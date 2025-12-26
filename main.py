import os
from flask import Flask

app = Flask(__name__)
version = os.getenv("APP_VERSION", "unknown")

@app.route('/')
def index():
    return 'Hello Pittsburgh Steelers {version}!'

app.run(host='0.0.0.0', port=8080)