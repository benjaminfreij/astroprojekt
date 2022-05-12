from flask import Flask, render_template

app = Flask(__name__)

app.config["FLASK_ENV"]="development"

@app.route('/')
def index():
    return render_template('sida.html')