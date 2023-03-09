from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/page1")
def page1():
    return "<p>page1</p>"

@app.route("/page2")
def page2():
    return "<p>page2</p>"

if __name__=="__main__":
    app.run()