from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/hovedmeny')
def hovedmeny():
    return "Fast mat"

@app.route('/ukesmeny')
def ukesmeny():
    return "her er ukens meny!"

@app.route('/kontakt')
def kontakt():
    return "trøbbel? kontakte disse folkene"


if __name__ == "__main__":
    app.run(port=5001)