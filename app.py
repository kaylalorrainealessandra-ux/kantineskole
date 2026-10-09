from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def home(): 
    return "Velkommen til Skole Kantina!"


if __name__ == "__main__":
    app.run(port=5001)