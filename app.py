from settings import app
from flask import render_template

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/base/")
def base():
    return render_template("base.html")



if __name__ == '__main__':
    app.run(debug=True)
