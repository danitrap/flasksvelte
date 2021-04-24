from flask import Flask, render_template, send_from_directory, request
from app import greet

app = Flask(__name__)

@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/greet", methods=["POST"])
def hello():
    return greet(request.json['name'])

#Create the main driver function
if __name__ == '__main__':
    #call the run method
    app.run(debug=True,host='0.0.0.0')