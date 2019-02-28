import os
from flask import Flask,redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("http://35.183.247.189:4503/content/we-retail/us/en.html", code=302)
    #print("DA")
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    ip = '35.183.247.189'
    port = '4503'
    key = 'xvfT9T4FRCWV=W@v?=+Q}GHL'
    command = "/usr/src/app/push_publisher.sh " + 'http://' + ip + ':' + port + '/crx/packmgr/service.jsp' + ' ' + key
    subprocess.call(command, shell=True)
    print("JHERE")
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
