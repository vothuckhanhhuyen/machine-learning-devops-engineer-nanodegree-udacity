from flask import Flask, session, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    user = request.args.get('user')
    return "Hello " + user


app.run(host='0.0.0.0', port=8000)

# curl "127.0.0.1:8000?user=Huyen"