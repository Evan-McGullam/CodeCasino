answercheck = 0
print("")
print("Here are our games. To pick one, type the number of the game you would like to play!")
while answercheck == 0:
    selection = input("1. Blackjack, 2. Hangman")
    if selection == "1":
      from subprocess import call
      def open_py_file():
          call(["python", "Blackjack.py"])
      open_py_file()
    elif selection == "2":
      from subprocess import call
      def open_py_file():
          call(["python", "Hangman.py"])
      open_py_file()
    else:
        print("Please enter a valid input.")
