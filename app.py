from flask import Flask, jsonify, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route("/")
def home():
    return "Welcome to the Temperature Converter App (Push 1 Active)!"

@app.route("/convert/c2f")
def convert_c2f():
    try:
        cels = float(request.args.get('celsius', 0))
        fahr = celsius_to_fahrenheit(cels)
        return jsonify(celsius=cels, fahrenheit=fahr)
    except ValueError:
        return jsonify(error="Invalid numerical input"), 400

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
