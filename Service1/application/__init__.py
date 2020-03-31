from flask import Flask, request
import requests
import os
from flask_mysqldb import MySQL

app = Flask(__name__)
# app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
# app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER')
# app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD')
# app.config['MYSQL_DB'] = os.environ.get('MYSQLDB')
# mysql = MySQL(app)

from application import routes