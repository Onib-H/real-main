import re
from datetime import datetime

def validate_first_name(first_name):
    regex = r'^[A-Za-z\s]+$'
    repeated_char_regex = r'(.)\1{2,}'
    max_length = 20

    if not first_name:
        return "First name is required."
    if not re.match(regex, first_name.strip()):
        return "First name must not contain special characters or numbers."
    if len(first_name.strip()) < 2:
        return "First name must be at least 2 characters long."
    if len(first_name.strip()) > max_length:
        return f"First name must be at most {max_length} characters long."
    if re.search(repeated_char_regex, first_name.strip()):
        return "First name must not contain repeated characters."
    return ""

def validate_middle_name(middle_name):
    regex = r'^[A-Za-z\s]+$'
    repeated_char_regex = r'(.)\1{2,}'
    max_length = 20

    if middle_name and not re.match(regex, middle_name.strip()):
        return "Middle name must not contain special characters or numbers."
    if middle_name and len(middle_name.strip()) < 2:
        return "Middle name must be at least 2 characters long."
    if middle_name and len(middle_name.strip()) > max_length:
        return f"Middle name must be at most {max_length} characters long."
    if middle_name and re.search(repeated_char_regex, middle_name.strip()):
        return "Middle name must not contain repeated characters."
    return ""

def validate_last_name(last_name):
    regex = r'^[A-Za-z\s]+$'
    repeated_char_regex = r'(.)\1{2,}'
    max_length = 20

    if not last_name:
        return "Last name is required."
    if not re.match(regex, last_name.strip()):
        return "Last name must not contain special characters or numbers."
    if len(last_name.strip()) < 2:
        return "Last name must be at least 2 characters long."
    if len(last_name.strip()) > max_length:
        return f"Last name must be at most {max_length} characters long."
    if re.search(repeated_char_regex, last_name.strip()):
        return "Last name must not contain repeated characters."
    return ""

def validate_birthday(birthday, age):
    if not birthday:
        return "Birthday is required."

    try:
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format."

    current_date = datetime.now()
    sixty_years_ago = datetime(1964, 1, 1)

    if birthday_date > current_date:
        return "Birthday cannot be a future date."

    if birthday_date < sixty_years_ago:
        return "The birthdate must not be earlier than January 1, 1964, based on app standards."

    calculated_age = current_date.year - birthday_date.year
    is_birthday_past_this_year = (
        current_date.month > birthday_date.month or
        (current_date.month == birthday_date.month and current_date.day >= birthday_date.day)
    )
    final_calculated_age = calculated_age if is_birthday_past_this_year else calculated_age - 1

    if final_calculated_age != int(age):
        return f"The age ({age}) does not match the birthday."

    return ""

def validate_age(age, birthday):
    if not age:
        return "Age is required."
    
    try:
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format for birthday."

    current_date = datetime.now()
    calculated_age = current_date.year - birthday_date.year

    # Check if the birthday has passed this year
    is_birthday_past_this_year = (
        current_date.month > birthday_date.month or
        (current_date.month == birthday_date.month and current_date.day >= birthday_date.day)
    )
    
    final_calculated_age = calculated_age if is_birthday_past_this_year else calculated_age - 1
    
    # Check if the provided age matches the calculated age based on the birthday
    if final_calculated_age != int(age):
        return f"The birthday ({birthday}) does not match the age."

    if int(age) < 10:
        return "Age must be at least 10."
    
    if int(age) > 60:
        return "Age must be less than or equal to 60."

    return ""

def validate_contact_number(contact_number):
    regex = r'^09\d{9}$'

    if not contact_number:
        return "Contact number is required."

    trimmed_contact_number = contact_number.strip()

    if not re.match(regex, trimmed_contact_number):
        return "Contact number must be a valid Philippine mobile number."

    if re.search(r'(\d)\1{3,}', trimmed_contact_number):
        return "Contact number must not contain 4 or more repeating digits."

    return ""

def validate_email(email):
    valid_providers = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com', 'icloud.com']
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|co|io|co\.uk)$'

    if not email:
        return "Email is required."

    if not re.match(email_regex, email.strip()):
        return "Invalid email format. Please use a valid email provider."

    domain = email.split('@')[1]

    if domain and domain not in valid_providers:
        return f"Invalid email format. {domain} is not a recognized email provider."

    if domain and re.search(r'\d', domain.split('.')[0]) and not domain.endswith('.co.uk'):
        return "Invalid email format. Domain should not contain numbers."

    return ""

def validate_username(username):
    username = username.strip()  # Trim leading/trailing spaces
    
    # Check if the username is provided
    if not username:
        return "Username is required."
    
    # Ensure the username does not contain spaces
    if " " in username:
        return "Username cannot contain spaces."
    
    # Length check (e.g., between 5 and 20 characters)
    if len(username) < 5 or len(username) > 20:
        return "Username must be between 5 and 20 characters."
    
    # Character restriction (only alphanumeric and underscores allowed)
    if not username.isalnum() and "_" not in username:
        return "Username can only contain letters, numbers, and underscores."
    
    return ""

def validate_password(password):
    password = password.strip()  # Trim leading/trailing spaces
    
    if not password:
        return "Password is required."
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    if not any(char in "!@#$%^&*()-_+=<>?/|{}[]" for char in password):
        return "Password must contain at least one special character."
    
    return ""

