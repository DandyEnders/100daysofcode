def format_name(first_name, last_name):
  if first_name == "" or last_name == "":
    return "You did not provide valid inputs."
  formatted_first_name = first_name.title()
  formatted_last_name = last_name.title()

  print(formatted_first_name, formatted_last_name)
  
formatted_string = format_name("John", "Doe")
print(formatted_string)
