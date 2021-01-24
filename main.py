from flask import Flask, render_template, request
import nomenclatura
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST","GET"])
def login():
    if request.method == "POST":
        return json.dumps({"output":nomenclatura.start(request.get_json())})
    else:
        return "hello"

if __name__ == "__main__":
    app.run()
