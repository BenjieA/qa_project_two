from flask import Flask, jsonify
import json
import requests
import random


app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def rand_stats():
    Strength=str(random.randint(10, 50))
    Endurance=str(random.randint(10, 50))
    Agility=str(random.randint(10, 50))
    Intelligence=str(random.randint(10, 50))
    Charisma=str(random.randint(10, 50))

    return jsonify ({'Strength' : Strength , 'Endurance' : Endurance , 'Agility' : Agility , 'Intelligence' : Intelligence , 'Charisma' : Charisma})

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5005, debug=True)
