from flask import render_template, request, redirect, url_for, session, flash, make_response
from flask import Blueprint


blog_blueprint = Blueprint('blog', __name__, template_folder='templates')

@blog_blueprint.route('/')
def index(): 
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.index'))

    response = make_response(render_template('blog.html'))
    response.headers['Cache-Control'] = 'no-store'
    return response 

