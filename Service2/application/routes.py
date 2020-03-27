from application import app
import random


@app.route('/prizetype', methods=['GET'])
def prizetype():

	list = ['good','average','bad']
	
	return list[random.randrange(2)]