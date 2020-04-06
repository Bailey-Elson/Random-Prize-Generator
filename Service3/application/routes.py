  
from application import app
import random
import requests
from flask import request 

@app.route('/randomprize', methods=['GET'])
def randomprize():
    prizelist = ["","","","","","",""]
    prize_type = request.args.get('ptype')
    print(prize_type)
    if prize_type == 'good':
        prizelist = ['an Ipad','a Ferrari','1,000,000 pounds','an Xbox','a years supply of food','a holiday to Miami','a new house']
    elif prize_type == 'average':
        prizelist = ['a chocolate bar','20 pounds','a new book','a free meal','a new top','a pair of sunglasses','some flowers']
    elif prize_type == 'bad':
        prizelist = ['nothing','a single sock','a used tissue','a broken Yo-Yo','out of date cheese','an empty box','a sheet of paper']
    
    prize = prizelist[random.randrange(7)]
    print(prize)
    
    return prize