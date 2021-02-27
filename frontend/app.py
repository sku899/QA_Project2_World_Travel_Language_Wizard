from flask import Flask, request, render_template
from flask_wtf import FlaskForm
import requests
from os import getenv
from random import randint
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TOP_SECRET_KEY'

class BasicForm(FlaskForm):
    submit = SubmitField('Next')

@app.route("/", methods=["GET", "POST"])
def home():
    form = BasicForm()
    result = requests.get("http://backend:5003/randomtemp")
    result_dict = result.json()
    word=result_dict["word"]
    country=" in " +result_dict["country"] + " is "
    translate= result_dict["translate"]
    return render_template('actions.html', form=form, word=word,country=country,translate= translate)

if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
