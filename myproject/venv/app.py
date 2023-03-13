from flask import Flask
from flask import render_template

app = Flask(__name__)

list = [
    "list1",
    "list2",
    "list3",
    "list4",
    "list5",
    "list6",
]

@app.route("/<name>")
def hello(name):
    return render_template('index.html',name=name,list=list)

if __name__=="__main__":
    app.run()