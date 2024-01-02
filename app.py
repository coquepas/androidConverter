from flask import Flask, redirect


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect("http://www.google.es")


