from application import app
from flask import render_template, request, Flask 
import requests
import random
from flask_mysqldb import MySQL
import os
# app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQLHOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQLUSER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQLPASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQLDB')
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    response = requests.get('http://localhost:5003/generateprize')
    output_sentence = response.text
    print(output_sentence)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO prizes(prize)VALUES(%s);",[output_sentence])
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', output_sentence = output_sentence, title = 'Home')