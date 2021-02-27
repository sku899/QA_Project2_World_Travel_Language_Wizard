from flask import Flask, jsonify
from os import getenv
from random import randint
import requests

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/randomtemp")
def random_generator_temp():
    countries = ['German', 'Spanish', 'French', 'Russian', 'Chinese', 'Portuguese','Hindi','Arabic','Japanese', 'Korean'] #10 countries

    welcome = {countries[0]: 'Willkommen', countries[1]: 'Bienvenida, Bienvenido', countries[2]:'Bienvenue, Bienvenu', \
        countries[3]:'Добро пожаловать', countries[4]:'欢迎', countries[5]:'Receber',countries[6]:'स्वागत हे',countries[7]:'أهلا بك', \
        countries[8]:'ようこそ',countries[9]:'어서 오십시오'}
    
    thankyou={countries[0]: 'Danke', countries[1]: 'Gracias', countries[2]:'Merci', \
        countries[3]:'Спасибо', countries[4]:'谢谢你', countries[5]:'Obrigada', countries[6]:'जी शुक्रिया',countries[7]:'شكرا لك', \
        countries[8]:'ありがとうございました',countries[9]:'감사합니다'}

    goodmoring={countries[0]: 'Guten Morgen', countries[1]: 'Buenos Días', countries[2]:'Comment allez-vous', \
        countries[3]:'доброе утро', countries[4]:'早上好', countries[5]:'Bom Dia', countries[6]:'शुभ प्रभात',countries[7]:'صباح الخير', \
        countries[8]:'おはようございます',countries[9]:'좋은 아침'}

    howareyou = {countries[0]: 'Wie geht es Ihnen', countries[1]: 'Cómo Estás', countries[2]:'Bonjour', \
        countries[3]:'как дела', countries[4]:'你好吗', countries[5]:'Como você está', countries[6]:'होर सुनाओ',countries[7]:'كيف حالك', \
        countries[8]:'お元気ですか',countries[9]:'어떻게 지내'}

    original_words = ['Welcome', 'Thank You','Good Morning', 'How are you']    
    translates = [welcome, thankyou, goodmoring, howareyou]
    country = requests.get("http://generator01:5001/random")
    translate = requests.get("http://generator02:5002/random")
    word = original_words[int(translate.text)-1]
    country = countries[int(country.text)-1]
    translate=translates[int(translate.text)-1][country]
    return jsonify(hello ='helloworld', country=country, word=word, translate=translate)


# 

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)
