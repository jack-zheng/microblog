from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Jack'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Today is a beautiful day'
            },
            {
                'author': {'username': 'Jack'},
                'body': 'Today I ride bike to home'
            }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)
