from application import app
import random
import requests


@app.route('/prizetype', methods=['GET'])
def prizetype():

	list = ['good','average','bad']
	
	return list[random.randrange(3)]