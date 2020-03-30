from application import app
import requests


@app.route('/generateprize', methods=['GET'])
def generateprize():
    ptype = requests.get('http://localhost:5001/prizetype')
    print(ptype.text)
    prize = requests.get('http://localhost:5002/randomprize?ptype='+ptype.text)
    
    output_sentence = "you won a "+ ptype.text + " prize, you won " + prize.text
    return output_sentence