from flask import Flask,render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"

from routes import *




if __name__ == "__main__":
    app.run(debug=True)