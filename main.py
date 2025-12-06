from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# لیست هدرها
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64)',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64)',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:69.0)',
        'Accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Debian; Linux x86_64; rv:76.0)',
        'Accept': '*/*'
    }
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running"}), 200

@app.route("/send", methods=["POST"])
def send_views():
    try:
        data = request.json
        url = data.get("url")
        count = int(data.get("count", 0))

        if not url:
            return jsonify({"error": "url missing"}), 400

        view = 0

        while view < count:
            h = random.choice(heads)
            try:
                r = requests.post(url, headers=h, timeout=3)
            except:
                r = None
            view += 1

        return jsonify({"status": "done", "views_sent": view})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
