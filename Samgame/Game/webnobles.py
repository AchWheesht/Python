import noblename_app
from flask import Flask

app = Flask(__name__)

nobles = noblename_app.NoblenameApp()

@app.route("/")
def index():
    return nobles.generate_name()

if __name__ == "__main__":
    app.run()
