  
from application import app
import random


@app.route('/randomprize', methods=['GET'])
def randomprize(prize_type):

	if prize_type == 'good':
        list = ['an Ipad','a Ferrari','£1,000,000','an Xbox','a year supply of food','a holiday to Miami','a new house']
    elif prize_type == 'average':
        list = ['a chocolate bar','£20','a new book','a free meal','a new top','a pair of sunglasses','some flowers']
    elif prize_type == 'bad':
        list = ['nothing','a single sock','a used tissue','a broken Yo-Yo','out of date cheese','an empty box','a sheet of paper']
	
	return list[random.randrange(6)]