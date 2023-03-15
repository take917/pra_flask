from flask import Flask
from flask import render_template

app = Flask(__name__)

memo_list = [
    {'title':'test01','body':'練習１'},
    {'title':'test02','body':'練習2'}
]


@app.route("/")
def top():
    return render_template('index.html',memo_list=memo_list)

if __name__=="__main__":
    app.run()