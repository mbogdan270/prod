from flask import Flask,redirect
import os

import subprocess

app = Flask(__name__)


@app.route('/')
def hello():

    return redirect("http://35.183.247.189:4503/content/we-retail/us/en.html", code=302)


if __name__ == '__main__':

    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
