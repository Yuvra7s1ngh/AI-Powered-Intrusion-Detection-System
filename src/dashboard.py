from flask import Flask, jsonify

app = Flask(__name__)
alerts = []

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(port=5000)