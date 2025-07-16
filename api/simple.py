from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def home():
    return {'status': 'working', 'message': 'API جاهز للعمل'}

@app.route('/test')
def test():
    return {'test': 'success'}

if __name__ == '__main__':
    app.run()
