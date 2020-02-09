import ast
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    data = request.get_json()
    data = ast.literal_eval(data)
    t = data["type"]
    print(t)
    return t

if __name__ == '__main__':
    app.run(host='0.0.0.0')
