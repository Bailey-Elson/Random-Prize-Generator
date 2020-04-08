import pytest
import urllib3
from flask import Flask
import os
import requests
from flask_mysqldb import MySQL
def test_service():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost/')
    assert 200 == r.status
def test_service1():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.134.136/')
    assert 200 == r.status
def test_getresponse():
    r = requests.get('http://35.230.134.136/')
    assert isinstance(r.text, str)
app=Flask(__name__)
app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']
mysql = MySQL(app)
def test_readSongsTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords = cur.execute("SELECT * FROM prizes;")
        mysql.connection.commit()
        cur.close()
        assert 0 < numRecords