# DAVID KIPNIS
# 06/26/2023
# Micro Blog - Application

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index() -> str:

    user = {'username': 'Dave'}

    posts = [
        {
            'author': {'username': 'Jim'},
            'body': 'Wowza'
        },
        {
            'author': {'username': 'Bob'},
            'body': "Jim's my bestest friend"
        }
    ]

    body = render_template('index.html', title='Home', user=user, posts=posts)

    return body
