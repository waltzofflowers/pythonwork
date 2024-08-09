def format_name_surname(f_name, l_name):
  
  f_name_title = f_name.title()

  l_name_title = l_name.title()

  return f_name_title, l_name_title

print("Welcome to the capitalizing world!..")

f_name = input("Your name is:")
l_name = input("Your surname is:")

formatted_f_name, formatted_l_name = format_name_surname(f_name, l_name)

print(f"Hello {formatted_f_name} {formatted_l_name}")