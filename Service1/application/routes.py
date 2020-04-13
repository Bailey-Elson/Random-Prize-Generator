from flask import Flask, request, render_template, url_for, redirect
from application import app
from flask_mysqldb import MySQL
import requests
import random

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    print("below\nbelow\nbelow\nbelow")
    response = requests.get('http://service4:5003/generateprize')
    output_sentence = response.text
    print(output_sentence)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO prizes(prize)VALUES(%s)",[output_sentence])
    mysql.connection.commit()
    cur.close()
    return render_template('index.html', output_sentence = output_sentence, title = 'Home')