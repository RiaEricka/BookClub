from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Book Club Main Page! <h1>HELLO<h1>"

if __name__ == "__main__":
    app.run(debug=True)
