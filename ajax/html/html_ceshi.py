from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/getsum", methods=["GET", "POST"])
def getsum():
    d = request.get_data()
    k = request.args
    n = request.args.get("myname")
    a = request.args.get("myage")
    print("n = ", n)
    print("a = ", a)
    print("d = ", d)
    print("k = ", k)
    info = {}
    info['name'] = "xiaoming"
    info["age"] = 8928
    return json.dumps(info)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
