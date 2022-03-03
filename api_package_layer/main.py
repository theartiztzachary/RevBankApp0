from flask import Flask, request

app: Flask = Flask(__name__)

@app.route("/greeting", methods=["GET"])
def hello_world():
   return "Hello world!"

app.run()