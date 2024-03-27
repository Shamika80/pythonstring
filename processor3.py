import re

def validate_name_length(name):
  
  if len(name) < 2:
    print(f"Error: Name must be at least 2 characters long. You entered '{name}'.")

def get_user_name():
 

  while True:
    first_name = input("Enter your first name: ")
    validate_name_length(first_name)
    
    last_name = input("Enter your last name: ")
    validate_name_length(last_name)
    
    # Exit the loop if both names are valid
    if len(first_name) >= 2 and len(last_name) >= 2:
      return first_name, last_name

def validate_password(password):




  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_number = any(char.isdigit() for char in password)
  
  if len(password) < 8:
    print("Error: Password must be at least 8 characters long.")
  elif not has_uppercase:
    print("Error: Password must contain at least one uppercase letter.")
  elif not has_lowercase:
    print("Error: Password must contain at least one lowercase letter.")
  elif not has_number:
    print("Error: Password must contain at least one number.")
  else:
    print("Password is valid!")

def get_user_password():
  
  while True:
    password = input("Enter your password (minimum 8 characters, containing uppercase, lowercase, and number): ")
    validate_password(password)
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
      return password

def validate_email(email):
 
  email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
  if not re.match(email_regex, email):
    print("Error: Invalid email address format. Please enter a valid email address.")

def get_user_email():
  
  while True:
    email = input("Enter your email address: ")
    validate_email(email)
    if re.match("email_regex, email"):
      return email

first_name, last_name = get_user_name()

password = get_user_password()
email = get_user_email()

print(f"Hello {first_name} {last_name}! Your password has been set and your email address is {email}.")