from flask import Flask, render_template, redirect, request
import sqlite3

from flask.wrappers import Request
from werkzeug.utils import redirect

# 名前を付ける
app = Flask(__name__)


@app.route('/')
def helloworld():
    return "hello world"


@app.route("/<name>")
def greet(name):
    return name + "さん, はろ～！"


@app.route("/template")
def template():
    py_name = "すなのもの"
    return render_template("index.html", name=py_name)

# /weather にアクセスしたら
# ↓
# 今日の天気は○○です。
# ↑
# と表示されるようにする
# ○○の部分は、パイソンによって渡す値によって、晴れなど変えられるように


@app.route("/weather")
def weather():
    py_tenki = "晴れ"
    return render_template("weather.html", tenki=py_tenki)


@app.route('/dbtest')
def dbtest():
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    # データベースの中のどのテーブルのどの項目の何番目のIDなのか
    c.execute("SELECT name, age, address FROM staff WHERE id = 2")
#    fetchone １件ずつデータをもってくる
    userInfo = c.fetchone()
    c.close()
    print(userInfo)
    return render_template('dbtest.html', html_staffInfo=userInfo)


@app.route('/add', methods=["GET"])
def add():
    return render_template('add.html')

# ポストメソッドに押されたときにメソッドに処理が……
# ネーム＝タスクが
# タスクという変数に入り


@app.route('/add', methods=["POST"])
def addPost():
    task = request.form.get("task")
    conn = sqlite3.connect('flasktest.db')
    c = conn.cursor()
    c.execute("INSERT INTO task VALUES(null, ?)", (task,))
    # データベースの保存
    conn.commit()
    c.close()
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
