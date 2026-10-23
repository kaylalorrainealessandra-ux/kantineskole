from flask import Flask, render_template
from meny import FASTE_RETT
from meny import UKESMENY
from meny import DRIKKE
from meny import DESSERT


app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/hovedmeny')
def hovedmeny():
    return render_template('hovedmeny.html', hovedmeny=FASTE_RETT)

@app.route('/ukesmeny')
def ukesmeny():
    return render_template('ukesmeny.html', ukesmeny=UKESMENY)

@app.route('/drikke')
def drikke():
    return render_template('drikke.html', drikke=DRIKKE)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)