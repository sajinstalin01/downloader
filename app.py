from flask import Flask, render_template, request, jsonify
from downloaders import instagram, facebook, tiktok, sharechat, pinterest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.json['url']
    try:
        if "instagram.com" in url:
            return jsonify(instagram.process(url))
        elif "facebook.com" in url:
            return jsonify(facebook.process(url))
        elif "tiktok.com" in url:
            return jsonify(tiktok.process(url))
        elif "sharechat.com" in url:
            return jsonify(sharechat.process(url))
        elif "pinterest.com" in url:
            return jsonify(pinterest.process(url))
        else:
            return jsonify({"error": "Unsupported platform"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
