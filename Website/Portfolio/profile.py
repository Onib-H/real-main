from flask import render_template, request, redirect, url_for, session, flash, make_response
from flask import Blueprint
import mysql.connector
from .validation_functions import validate_first_name, validate_middle_name, validate_last_name, validate_birthday, validate_age, validate_contact_number, validate_email


profile_blueprint = Blueprint('profile', __name__, template_folder='templates')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'users_db',
    'auth_plugin': 'mysql_native_password'
}


@profile_blueprint.route('/')
def index(): 
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.index'))
    
    # Fetch user information from the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users_info where id = 21')
    data = cursor.fetchall()
    
    for row in data:
        if 'birthday' in row and row['birthday']:
            # Format birthday directly (no need to parse)
            row['birthday'] = row['birthday'].strftime('%B %d, %Y')

    
    # Close cursor and connection
    cursor.close()
    conn.close()
    
    response = make_response(render_template('profile.html', data=data))
    response.headers['Cache-Control'] = 'no-store'
    return response


@profile_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.index'))
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    errors = {}  # Dictionary to store validation errors

    if request.method == 'POST':
        # Get form data
        firstname = request.form['firstname'].strip()
        middlename = request.form['middlename'].strip()
        lastname = request.form['lastname'].strip()
        birthday = request.form['birthday'].strip()
        age = request.form['age'].strip()
        contact_number = request.form['contact_number'].strip()
        email = request.form['email'].strip()

        # Validate form fields
        errors['firstname'] = validate_first_name(firstname)
        errors['middlename'] = validate_middle_name(middlename)
        errors['lastname'] = validate_last_name(lastname)
        errors['birthday'] = validate_birthday(birthday, age)
        errors['age'] = validate_age(age, birthday)
        errors['contact_number'] = validate_contact_number(contact_number)
        errors['email'] = validate_email(email)

        # If no errors, proceed with the update
        if not any(errors.values()):
            try:
                cursor.execute('''
                    UPDATE users_info 
                    SET firstname=%s, middlename=%s, lastname=%s, birthday=%s, age=%s, contact_number=%s, email=%s
                    WHERE id=%s
                ''', (firstname, middlename, lastname, birthday, age, contact_number, email, id))
                conn.commit()
                return '''
                <script>
                    alert('Data updated successfully');
                    window.location.href = "{}";
                </script>
                '''.format(url_for('profile.index'))
            except mysql.connector.Error as e:
                return f"Updating data failed! Error: {str(e)}"
        # If there are errors, re-render the form with errors
        return render_template('profile_update.html', data=request.form, errors=errors)
    
    else:
        try:
            cursor.execute('SELECT * FROM users_info WHERE id=%s', (id,))
            columns = [column[0] for column in cursor.description]
            data = dict(zip(columns, cursor.fetchone()))
            if not data:
                return 'Data not found!', 404
            return render_template('profile_update.html', data=data, errors=errors)
        except mysql.connector.Error as e:
            return f"Fetching data failed! Error: {str(e)}"
        finally:
            cursor.close()
            conn.close()
