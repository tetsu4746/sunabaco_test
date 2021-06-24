from os import name
from flask import Flask, render_template, request, redirect
import sqlite3
import session

from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "sunabacoT"


@app.route('/task_list')
def index():
    conn = sqlite3.connect('tasklist.db')
    c = conn.cursor()
    c.execute("SELECT * FROM task")
    task_list_py = []
    for row in c.fetchall():
        task_list_py.append(
            {"tpl_id": row[0], "tpl_task": row[1], "tpl_user_id": row[2]})
    c.close()
    print(task_list_py)
    return render_template('task.html', tpl_task_list=task_list_py)


@app.route('/regist')
def regist_get():
    return render_template('regist.html')


@app.route('/regist', methods=['POST'])
def regist_post():
    name = request.form.get("member_name")
    password = request.form.get("member_password")
    print(name)
    print(password)
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("INSERT INTO member VALUES(null,?,?)", (name, password))
    conn = commit()
    c.close()
    return ridirect("/task_list")


@app.route('/login')
def login_get():
    return render_template('regist.html')


@app.route('login', method=['POST'])
def regist_post():
    name = request.form.get("member_name")
    password = request.form.get("member_password")
    print(name)
    print(password)
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("SELECT id FROM member WHERE name = ? AND password = ?",
              (name, password))
    user_id = c.fetchone()
    conn = commit()
    c.close()
       if user_id is None:
            return render_template("login.html")
        else:
			session["user_id"] = user_id
            return redirect("task_list")


if __name__ == "__main__":
    app.run(debug=True)
