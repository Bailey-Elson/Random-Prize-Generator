from application import app
import requests


@app.route('/generateprize', methods=['GET'])
def generateprize():
    prize_type, prize = requests.get('http://localhost:5002/randomprize')
    output_sentence = "You got a "+ prize_type.text + " prize, you won " + prize.text
    return output_sentence