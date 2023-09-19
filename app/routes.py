from flask import render_template
from app import app


@app.route('/')
def index():
    user = {"username": "prince hope"}
    return render_template('index.html', user=user)

@app.route('/about')
def about():
    title = "about"
    todos = ["laundry", "cook supper", "take jog"]
    return render_template('about.html', title=title, todos=todos)

@app.route('/posts/<int:id>')
def posts(id):
    return f"this is my post of id {id}"