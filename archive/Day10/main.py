def format_name(first_name: str, last_name: str) -> str:
  """Take a first and last name and format it to
  return the title case version of the name.

  Args:
      first_name (str): first name
      last_name (str): last name

  Returns:
      str: formatted name
  """
  if first_name == "" or last_name == "":
    return "You did not provide valid inputs."
  formatted_first_name = first_name.title()
  formatted_last_name = last_name.title()
  
  return f"{formatted_first_name} {formatted_last_name}"
  
formatted_string = format_name("John", "Doe")
print(formatted_string)
