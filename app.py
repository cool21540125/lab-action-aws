from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Hello 1124 1447"


if __name__ == "__main__":
    app.run()
