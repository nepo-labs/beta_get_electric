import json
import os
import re
from logging.config import dictConfig

import flask

from flask import Flask, request, render_template, send_from_directory
from datetime import datetime, timedelta


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = flask.Flask(__name__)


@app.route('/get-electric/terms-of-use',methods=['GET'])
def terms_of_use():
    return render_template('terms-of-use.html')

@app.route('/get-electric/privacy-policy',methods=['GET'])
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/get-electric/get-sms',methods=['GET'])
def get_sms():
    return "755819"


if __name__ == '__main__':
    app.run(debug=True)
