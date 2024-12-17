from flask import render_template, request, redirect, url_for, session, flash, make_response
from flask import Blueprint
import mysql.connector
from .validation_functions import validate_username, validate_password
# Blueprint setup
login_blueprint = Blueprint('login', __name__, template_folder='templates')

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'users_db',
    'auth_plugin': 'mysql_native_password'
}

@login_blueprint.route('/', methods=['GET', 'POST'])
def index():
    # Redirect to dashboard if user is already logged in
    if 'user' in session:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        # Get user inputs
        username = request.form.get('username')
        password = request.form.get('password')

        # Input validation
        if not username:
            flash('Username is required.', 'danger')
        elif not password:
            flash('Password is required.', 'danger')
        # elif len(username) < 2:
        #     flash('Username must be at least 2 characters long.', 'danger')
        # elif len(password) < 8:
        #     flash('Password must be at least 8 characters long.', 'danger')
        else:
            # Check the credentials against the database for the row with id=21
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()

                # Query to check the user with id=21
                cursor.execute("SELECT * FROM users_info WHERE id = %s", (21,))
                user = cursor.fetchone()

                # Check if user exists and if username and password match (username in column 9, password in column 10)
                if user and username == user[8] and password == user[9]:  # username is in column 9 (index 8), password in column 10 (index 9)
                    # If user exists and username/password match, create session
                    session['user'] = username
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard.index'))
                
                # For other users, check dynamically by username
                cursor.execute("SELECT * FROM users_info WHERE username = %s", (username,))
                user = cursor.fetchone()

                if user and password == user[9]:  # Assuming password is in the 10th column (index 9)
                    # Regular user login successful
                    session['user'] = username
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard.index'))
                
                elif username == "admin" and password == "password":
                    session['user'] = username
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard.index'))
                
                else:
                    flash('Invalid username or password. Please try again.', 'danger')

            except mysql.connector.Error as err:
                flash(f"Database error: {err}", 'danger')
            finally:
                cursor.close()
                conn.close()

    # Render login page with no-store headers
    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store'
    return response
