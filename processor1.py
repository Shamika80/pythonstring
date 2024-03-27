def validate_name_length(name):
  
  if len(name) < 2:
    print(f"Error: Name must be at least 2 characters long. You entered '{name}'.")

def get_user_name():
  
  while True:
    first_name = input("Enter your first name: ")
    validate_name_length(first_name)
    
    last_name = input("Enter your last name: ")
    validate_name_length(last_name)
    
    if len(first_name) >= 2 and len(last_name) >= 2:
      return first_name, last_name

first_name, last_name = get_user_name()

print(f"Hello {first_name} {last_name}!")