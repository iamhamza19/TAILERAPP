from flask import Flask, render_template, Response, jsonify, current_app, request
from htmlmin import minify
import mysql.connector
from datetime import datetime, timedelta
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
import base64
import time
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
from PIL import Image
from io import BytesIO
import random
import re

app = Flask(__name__)

def pageSettings():
    return {
        "static_url":app.static_url_path
    }

@app.route('/about')
def about():
    data = []
    return render_template('index.html', data=data, specified = None)


@app.route('/')
def index():
    data = []
    return render_template('index.html', data=data, pageSettings=pageSettings(), specified = None)


@app.route('/test/app')
def index_1():
    data = []
    return render_template('test.html', data=data, pageSettings=pageSettings(), specified = None)


    
if __name__ == '__main__': 
    # app.run()
    app.run(debug=True)
