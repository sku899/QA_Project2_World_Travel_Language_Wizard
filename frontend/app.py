from flask import Flask, request, render_template
from flask_wtf import FlaskForm
import requests
from os import getenv
from random import randint
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TOP_SECRET_KEY'

class BasicForm(FlaskForm):
    submit = SubmitField('Start')

@app.route("/", methods=["GET", "POST"])
def home():
    form = BasicForm()
    if  form.submit.label.text == '':
        msg = "Welcome"
        hostname = getenv("HOSTNAME")
        backend01_hostname = requests.get("http://generator01:5001/hostname")
        random = requests.get("http://generator01:5001/random")

        backend_hostname = requests.get("http://backend:5003/hostname")
        result = requests.get("http://backend:5003/random")
        colours =["blue","green", "yellow"]
        colour = colours[randint(0,2)]
    else:
        result2 = requests.get("http://backend:5003/randomtemp")
        result2_dict = result2.json()
        msg = result2_dict["word"] + " in " +result2_dict["country"] + " is " +result2_dict["translate"]
        return render_template('actions.html', form=form, word=result2_dict["word"],country=" in " +result2_dict["country"] + " is ",translate= result2_dict["translate"] )
    form.submit.label.text = 'Next'
    return render_template('actions.html', form=form, message= msg)
    # return result2_dict["word"] + " in " +result2_dict["country"] + " is " +result2_dict["translate"]
    # return f"<body style='background-color:{colour};'>\n<h1>Hello.</h1>\n\n<h2>I'm currently running in {hostname}.</h2>\n\n" + \
    #  f"<h2>The backend I'm chatting with is running in {backend01_hostname.text}</h2>\n\n<h3>The backend gave me this to show you: {random.text}</h3>\n\n"+ \
    #      f"<h2>The backend I'm chatting with is running in {backend_hostname.text}</h2>\n\n<h3>The backend gave me this to show you: {random.text}</h3>"

if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
