  
from application import app
import random
import requests
from flask import request 

@app.route('/randomprize', methods=['GET'])
def randomprize():

    prize_type = request.args.get('ptype')
    print(prize_type)
    if prize_type == 'good':
        list = ['an Ipad','a Ferrari','1,000,000 pounds','an Xbox','a years supply of food','a holiday to Miami','a new house']
    elif prize_type == 'average':
        list = ['a chocolate bar','20 pounds','a new book','a free meal','a new top','a pair of sunglasses','some flowers']
    elif prize_type == 'bad':
        list = ['nothing','a single sock','a used tissue','a broken Yo-Yo','out of date cheese','an empty box','a sheet of paper']
    prize = list[random.randrange(7)]
    print(prize)
    
    return prize