from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Argo CD v9.0 - Blue/Green Deployment!'

app.run(host='0.0.0.0', port=8080)