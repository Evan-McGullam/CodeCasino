enter = 0
print("Ahem ~ Welcome to Mc's Code Casino!")
print("Here we offer a variety(2) of games to play!")
while enter == 0:
  x = input("If you would like to enter the game floor, type 'Yes', if not type 'No'.")
  print("")
  if x.lower() == "yes":
    print("Welcome. Come on in!")
    enter = 1
    from subprocess import call
    def open_py_file():
        call(["python", "index.py"])
    open_py_file()
  elif x.lower() == "no":
    print("Feel free to come back any time!")
    y = input("Would you like to re-enter? Yes or No?")
    if y.lower() == "no":
      print("")
      print("Okay, have a nice day!")
      enter = 1
  else:
    print("Please enter a valid input. Only 'Yes' or 'No' are accepted.")
