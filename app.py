from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    data = request.get_json()
    type = data["type"]
    print(type)
    return type

if __name__ == '__main__':
    app.run(host='0.0.0.0')