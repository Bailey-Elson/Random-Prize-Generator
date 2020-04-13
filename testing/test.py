import pytest
import urllib3
from flask import Flask
import os
import requests
import csv
from flask_mysqldb import MySQL
def test_service():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://localhost/')
    assert 200 == r.status
def test_getresponse():
    r = requests.get('http://localhost/')
    assert isinstance(r.text, str)
def test_serviceworker():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.154.50/')
    assert 200 == r.status
def test_getresponseworker():
    r = requests.get('http://35.230.154.50/')
    assert isinstance(r.text, str)
app=Flask(__name__)
app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']
mysql = MySQL(app)
def test_readPrizeTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords = cur.execute("SELECT * FROM prizes;")
        mysql.connection.commit()
        cur.close()
        assert 0 < numRecords
def test_addPrizeTable():
    with app.app_context():
        cur = mysql.connection.cursor()
        numRecords1 = cur.execute("SELECT * FROM prizes;")
        mysql.connection.commit()
        cur.execute("INSERT INTO prizes(prize)VALUES('you won a test prize, you won a test');")
        mysql.connection.commit()
        numRecords2 = cur.execute("SELECT * FROM prizes;")
        mysql.connection.commit()
        cur.close()
        assert numRecords1 + 1 == numRecords2
def test_csvfile():
    file = open("/home/Admin/projects/SFIA2/SFIA2/Service3/application/prizes.txt")
    reader = csv.reader(file)
    lines= len(list(reader))
    assert lines == 3
def test_csvfile2():
    for row in open("/home/Admin/projects/SFIA2/SFIA2/Service3/application/prizes.txt"):
        coloumnlist = str(row)
        coloumnlist = coloumnlist.split(",")
    assert len(coloumnlist) == 7