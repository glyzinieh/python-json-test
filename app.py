import ast
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    data = request.data.decode()
    data = ast.literal_eval(data)
    TYPE = data["type"]
    print(TYPE)
    return TYPE

if __name__ == '__main__':
    app.run(host='0.0.0.0')
