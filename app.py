from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_world():
    secret = os.getenv("DEMO_SECRET", "default name")
    return f"Hello 1122 1456, {secret}"


if __name__ == "__main__":
    app.run()
