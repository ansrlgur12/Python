from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello() :
    return "안녕하세요. 플라스크를 사용해봅니다."