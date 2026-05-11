from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    direction = data.get("direction", "en-kn")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    source, target = direction.split("-")
    translated = GoogleTranslator(source=source, target=target).translate(text)
    return jsonify({"translated": translated})


if __name__ == "__main__":
    app.run(debug=True)
