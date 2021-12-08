from . import db

class ToDo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, index=True)
    content = db.Column(db.String)

def create_todo(content: str):
    todo = ToDo(content=content)
    db.session.add(todo)
    db.session.commit()
    db.session.refresh(todo)
    return todo


def get_todo(item_id: int):
    return ToDo.query.get_or_404(item_id)

def update_todo(item_id: int, content: str):
    todo = get_todo(item_id)
    todo.content = content
    db.session.commit()
    db.session.refresh(todo)
    return todo


def get_todos(skip: int = 0, limit: int = 100):
    return ToDo.query.offset(skip).limit(limit).all()

def delete_todo(item_id: int):
    todo = get_todo(item_id)
    db.session.delete(todo)
    db.session.commit()

