from . import app

from flask import request,render_template

from .models import *

@app.get("/")
def home():
    todos = get_todos()
    return render_template("home.html",todos=todos,title="Home")


@app.post("/add")
def post_add():
    content = request.form['content']
    todo = create_todo(content=content)
    return render_template("todo/item.html",todo=todo)


@app.get("/edit/<item_id>")
def get_edit(item_id: int):
    todo = get_todo(item_id)
    return render_template("todo/form.html", todo=todo)


@app.put("/edit/<item_id>")
def put_edit(item_id: int):
    content = request.form['content']
    todo = update_todo(item_id, content)
    return render_template("todo/item.html", todo=todo)


@app.delete("/delete/<item_id>")
def delete(item_id: int):
    delete_todo(item_id)
    return ""
    # todos = get_todos()
    # return render_template("todo/items.html",todo=todos)
