from flask import Flask
import json
import request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    param = json.loads(request.json)
    type = param.get('type')
    print(type)
    return type

if __name__ == '__main__':
    app.run(host='0.0.0.0')