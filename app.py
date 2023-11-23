from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Hello 1123 1200"


if __name__ == "__main__":
    app.run()
