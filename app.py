from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Это простое Flask-приложение."

@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({"sum": a + b})
    except ValueError:
        return jsonify({"error": "Передайте числа в параметрах 'a' и 'b'."}), 400

if __name__ == '__main__':
    app.run(debug=True, port='8080')