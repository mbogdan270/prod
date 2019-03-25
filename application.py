from flask import Flask,redirect
import os
from flask import request
from flask import jsonify
import subprocess

import re
import sys
import unicodedata
import string
import time
from threading import Thread
app = Flask(__name__)
numberofrequests = {}
start_time = time.time()
blacklist = {}
cookies = {
    'cookiebanner-accepted': '1',
    'optinmodal': 'shown',
    '__utmt': '1',
    '__utma': '67803593.580391096.1496747284.1497281718.1497345596.7',
    '__utmb': '67803593.1.10.1497345596',
    '__utmc': '67803593',
    '__utmz': '67803593.1496747284.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'Origin': 'http://www.ipvoid.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://www.ipvoid.com/',
    'Connection': 'keep-alive',
}
def get_elapsed_time():

    elapsed_time = time.time() - start_time
    if elapsed_time > 10:
        global start_time
        start_time = time.time()
        global numberofrequests
        numberofrequests = {}
def check(i):
    data = [('ip', i),]
    g=requests.post('http://www.ipvoid.com/ip-blacklist-check/', headers=headers, cookies=cookies, data=data)
    string1 = unicodedata.normalize('NFKD', g.text).encode('ascii','ignore')
    r = string1.translate(string.maketrans("\n\t\r", "   "))
    final_string = str(re.findall(r'BLACKLISTED \d+\/\d+',str(r)))
    if("BLACKLISTED" in final_string):
        return 1
    if i in blacklist:
        return 1
    return 0
def count(ip):
    get_elapsed_time()

    if ip in numberofrequests:
        numberofrequests[ip] += 1
    else:
        numberofrequests[ip] = 1

def check_ddos(ip):
    if numberofrequests[ip] > 50:
        blacklist[ip] = 1
@app.route('/')
def hello():
    
    var = check(request.remote_addr)
    count(request.remote_addr)
    check_ddos(request.remote_addr)
    print(numberofrequests[request.remote_addr])
    if var == 1:
        return "forbidden"
    else:
        return redirect("http://lasttop.adobecemcloud.net/home", code=302)



if __name__ == '__main__':

    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
