from flask import render_template, request, redirect, url_for, session, flash, make_response
from flask import Blueprint


dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_blueprint.route('/')
def index(): 
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.index'))

    response = make_response(render_template('dashboard.html'))
    response.headers['Cache-Control'] = 'no-store'
    return response

@dashboard_blueprint.route('/logout')
def logout():
    
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login.index'))
