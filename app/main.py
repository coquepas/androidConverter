from flask import Flask, redirect
from android.permissions import request_permissions, Permission
request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect("http://www.google.es")

if __name__=="__main__":
    app.run(debug=False,port=8080)
