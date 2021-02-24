from flask import Flask, jsonify
from os import getenv
from random import randint
import requests
# from p2_tables import db, Events

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/random")
def random_generator():
    countries = {'1': 'German', '2':'Spain', '3':'France', '4':'Russia', '5':'China', '6':'Portugal','7':'India','8':'Arabic'}

    welcome = {'German': 'Willkommen', 'Spain': 'Bienvenida, Bienvenido', 'France':'Bienvenue, Bienvenu', \
        'Russia':'Добро пожаловать', 'China':'欢迎', 'Portugal':'Receber','India':'स्वागत हे','Arabic':'أهلا بك'}
    
    thankyou={'German': 'Danke', 'Spain': 'Gracias', 'France':'Merci', \
        'Russia':'Спасибо', 'China':'谢谢你', 'Portugal':'Obrigada', 'India':'जी शुक्रिया','Arabic':'شكرا لك'}

    goodmoring={'German': 'Guten Morgen', 'Spain': 'Buenos Días', 'France':'Comment allez-vous', \
        'Russia':'доброе утро', 'China':'早上好', 'Portugal':'Bom Dia', 'India':'शुभ प्रभात','Arabic':'صباح الخير'}

    howareyou = {'German': 'Wie geht es Ihnen', 'Spain': 'Cómo Estás', 'France':'Bonjour', \
        'Russia':'как дела', 'China':'你好吗', 'Portugal':'Como você está', 'India':'होर सुनाओ','Arabic':'كيف حالك'}

    original_words = {'1': 'Welcome', '2':'Thank You', '3': 'Good Morning', '4': 'How are you'}    
    translates = [welcome, thankyou, goodmoring, howareyou]
    #backend01_hostname = requests.get("http://backend01:5001/hostname")
    country = requests.get("http://generator01:5001/random")
    translate = requests.get("http://generator02:5002/random")
     #r = str(randint(1,8))
    fontcolor=['<b style="color:blue">', '<b style="color:black">', '<b style="color:green">']
    fontsize = ['<p style="font-size:30px">', '<p style="font-size:20px">', '<p style="font-size:40px">']
    result = fontcolor[0]+fontsize[0] + '"' + original_words[translate.text]+'"'+"</p></b><br>" +  \
                fontcolor[1]+fontsize[1] + ' in  ' +  countries[country.text]  +' is ' +"</p></b><br>" +  \
                fontcolor[2]+fontsize[2] + translates[int(translate.text)-1][countries[country.text]]+"</p></b><br>"

    return result
    #return f"Welcome in {countries[r.text]} is {welcome[countries[r.text]]}"

# 
@app.route("/randomtemp")
def random_generator_temp():
    countries = {'1': 'German', '2':'Spain', '3':'France', '4':'Russia', '5':'China', '6':'Portugal','7':'India','8':'Arabic'}

    welcome = {'German': 'Willkommen', 'Spain': 'Bienvenida, Bienvenido', 'France':'Bienvenue, Bienvenu', \
        'Russia':'Добро пожаловать', 'China':'欢迎', 'Portugal':'Receber','India':'स्वागत हे','Arabic':'أهلا بك'}
    
    thankyou={'German': 'Danke', 'Spain': 'Gracias', 'France':'Merci', \
        'Russia':'Спасибо', 'China':'谢谢你', 'Portugal':'Obrigada', 'India':'जी शुक्रिया','Arabic':'شكرا لك'}

    goodmoring={'German': 'Guten Morgen', 'Spain': 'Buenos Días', 'France':'Comment allez-vous', \
        'Russia':'доброе утро', 'China':'早上好', 'Portugal':'Bom Dia', 'India':'शुभ प्रभात','Arabic':'صباح الخير'}

    howareyou = {'German': 'Wie geht es Ihnen', 'Spain': 'Cómo Estás', 'France':'Bonjour', \
        'Russia':'как дела', 'China':'你好吗', 'Portugal':'Como você está', 'India':'होर सुनाओ','Arabic':'كيف حالك'}

    original_words = {'1': 'Welcome', '2':'Thank You', '3': 'Good Morning', '4': 'How are you'}    
    translates = [welcome, thankyou, goodmoring, howareyou]
    #backend01_hostname = requests.get("http://backend01:5001/hostname")
    country = requests.get("http://generator01:5001/random")
    translate = requests.get("http://generator02:5002/random")
     #r = str(randint(1,8))
    fontcolor=['<b style="color:blue">', '<b style="color:black">', '<b style="color:green">']
    fontsize = ['<p style="font-size:30px">', '<p style="font-size:20px">', '<p style="font-size:40px">']
    result =  jsonify({"message":"No ids provided.",
                    "category":"error"})
    return jsonify(hello ='helloworld', country=countries[country.text], word=original_words[translate.text], translate=translates[int(translate.text)-1][countries[country.text]])

    # return jsonify(hello='world')


# 

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5003, debug = True)
