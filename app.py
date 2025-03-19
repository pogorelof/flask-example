from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Это простое Flask-приложение."
@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

if __name__ == '__main__':
    app.run(debug=True, port='8080')