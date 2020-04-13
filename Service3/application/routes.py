  
from application import app
import random
import requests
from flask import request 
import csv


@app.route('/randomprize', methods=['GET'])
def randomprize():
    # prizelist = ["","","","","","",""]
    prizetype = request.args.get('ptype')
    prizenum = random.randrange(0,6)
    with open('/opt/service3/application/prizes.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = -1
        for row in csv_reader:
            line_count += 1
            if line_count == 0 and prizetype == "good":
                prize = str(row[prizenum])
            elif line_count == 1 and prizetype == "average":
                prize = str(row[prizenum])
            elif line_count == 2 and prizetype == "bad":
                prize = str(row[prizenum])
    # if prize_type == 'good':
    #     prizelist = ['an Ipad','a Ferrari','1,000,000 pounds','an Xbox','a years supply of food','a holiday to Miami','a new house']
    # elif prize_type == 'average':
    #     prizelist = ['a chocolate bar','20 pounds','a new book','a free meal','a new top','a pair of sunglasses','some flowers']
    # elif prize_type == 'bad':
    #     prizelist = ['nothing','a single sock','a used tissue','a broken Yo-Yo','out of date cheese','an empty box','a sheet of paper']
    
    # prize = prizelist[random.randrange(7)]
    print(prize)
    
    return prize