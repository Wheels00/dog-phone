from email.policy import default
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FormField, FieldList
from wtforms.validators import Length, Regexp
from wtforms.widgets import TextArea
import json


app = Flask(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'ned3000'

# Flask-Bootstrap requires this line
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET', 'POST'])
def numbers():
    form = buildPhoneNumberForm()
    if form.validate_on_submit():
        data = form.data
        with open('storage/contacts.json', 'w+') as f:
            json.dump(data, f)
    return render_template('contacts.html',form=form)

def buildPhoneNumberForm():
    with open('storage/contacts.json', 'w+') as f:
        try:
            storage = json.load(f)
        except:
            storage = {}
    class PhoneNumberForm(FlaskForm):
        phonevalidators = [
        Regexp('[0-9]*', message="Phone number must be only numbers"),
        Length(min=0, max=10, message="Phone number must be betwen 0 & 10 digits")]
        name = StringField('Name',   default=storage.get('name',""))
        ph = StringField('Phone', validators=phonevalidators, default=storage.get('ph', ""))
        delay = StringField('Delay (mins)', validators=phonevalidators, default=storage.get('delay', ""))
    class PhoneNumberListForm(FlaskForm):
        numberlist = FieldList(FormField(PhoneNumberForm), min_entries=1)
        submit = SubmitField('Submit')
    return PhoneNumberListForm()

@app.route('/test', methods=['GET', 'POST'])
def test():
    form = buildMessageTestForm()
    if form.validate_on_submit():
        data = form.data
        with open('storage/test.json', 'w+') as f:
            json.dump(data, f)
    return render_template('test.html',form=form)

def buildMessageTestForm():
    with open('storage/test.json', 'w+') as f:
        try:
            storage = json.load(f)
        except:
            storage = {}
    class MessageTestForm(FlaskForm):
        testmessage = StringField('test message',   default=storage.get('testmessage',""))
        submit = SubmitField('Submit')
    return MessageTestForm()

@app.route('/wifi', methods=['GET', 'POST'])
def wifi():
    form = buildWifiForm()
    if form.validate_on_submit():
        data = form.data['text']
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", 'w') as f:
            f.write(data)
    return render_template('wifi.html',form=form)

def buildWifiForm():
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", 'r') as f:
        storage = f.read()
    class WifiForm(FlaskForm):
        text = StringField('text',  widget=TextArea(),  default=storage)
        submit = SubmitField('Submit')
    return WifiForm()

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

