from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    secret = os.getenv("DEMO_SECRET", "default name")
    return f"Hello, {secret}"


if __name__ == "__main__":
    app.run()
