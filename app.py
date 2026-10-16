from flask import Flask, render_template
from meny import MENU_ITEMS

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/hovedmeny')
def hovedmeny():
    return render_template('hovedmeny.html', meny=MENU_ITEMS)

@app.route('/ukesmeny')
def ukesmeny():
    return render_template('ukesmeny.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)