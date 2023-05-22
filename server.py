from flask import Flask, send_from_directory
from flask_cors import CORS
import random

app = Flask(__name__, static_folder='client/public')
CORS(app)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/", defaults={"path": ''})
@app.route("/<path:path>")
def home(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
