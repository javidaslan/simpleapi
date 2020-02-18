from flask import Flask, render_template, request, jsonify
import rook

app = Flask(__name__)


@app.route("/")
def index():
    """
    Main endpoint
    """
    return "Hello"


@app.route("/test")
def test():
    """
    test endpoint
    :return:
    """
    name = "Javid"
    surname = "Aslanov"
    full_name = "{} {}".format(name, surname)
    print(full_name)
    return full_name


if __name__ == "__main__":
    rook.start(token='dd0f1be251f3017e3e9da1555b9cd2fc9a0dddf103022a29f5342fff8af3b4b4')
    app.run(host="0.0.0.0", port=8080, threaded=True)