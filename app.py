import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.get("/")
def home():
    return send_from_directory(".", "index.html")

@app.get("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
