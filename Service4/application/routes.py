from application import app
import requests


@app.route('/generateprize', methods=['GET'])
def generateprize():
    prizetype = requests.get('http://localhost:5001/prizetype')
    prize = requests.get('http://localhost:5002/randomprize')
    output_sentence = "You got a "+ prizetype.text + " prize, you won " + prize.text
    return output_sentence