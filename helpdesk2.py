def parse_command(user_input):
 

  commands = {
      "help": "I can help you with using our application. How can I assist you today?",
      "issue": "I can help troubleshoot any issues you're facing. Please describe the problem in detail.",
      "contact support": "For more complex issues, you can contact our support team at [insert support email address here].",
  }

  issue_categories = {
      "login": "Login Issues",
      "performance": "Performance Issues",
      "error": "Error Messages",
      "bug": "Bugs",
  }

  user_input = user_input.lower()  
  words = user_input.split()  

  if words[0] in commands or any(word in commands for word in words):  #
    for command, response in commands.items():
      if command in user_input:
        print(response)

        if command == "issue": 
          for keyword, category in issue_categories.items():
            if keyword in user_input:
              print(f"Category: {category}")
              break  

        break 

  else:
    print("I didn't recognize that command. Here are some helpful commands: 'help', 'issue', 'contact support'")


user_input = input("How can I help you today? ")
parse_command(user_input)