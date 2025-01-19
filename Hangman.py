import random

wordbank = ["tech", "computer", "python", "chair", "table", "mouse", "keyboard", "monitor", "mousepad", "printer", "monitor", "smart", ] #add more
theword = random.choice(wordbank)
lives = 7
guessloop = 0
continuex = 1

print("Welcome to Hangman!")
print("Try to guess the word, you have 7 lives. Choose wisely!")
print("--------------------------------------------------")
print("The word is", len(theword), "letters long.")

# Create an empty list to store the guessed letters
board = ["_"] * len(theword)
print(" ".join(board))

while guessloop == 0:
  guess = input("Guess!").lower()
  found = False  # Flag to track if the guessed letter is in the word

  # Check each letter in the word
  for i in range(len(theword)):
    if guess == theword[i]:
      board[i] = guess  # Update the board with the guessed letter
      found = True
    elif (theword) == (guess):
      print("You win!")
      guessloop = 1
      continuex = 2
      break
      
  if continuex == 1:
    if found:
      print(" ".join(board))  # Print the updated board
      if "_" not in board:  # Check if all letters have been guessed
        print("You win! The word was:", theword)
        guessloop = 1  # End the game loop
    else:
      lives -= 1  # Decrement lives if the guessed letter is not in the word
      print("Incorrect guess. You have", lives, "lives left.")
      print(" ".join(board))  # Print the board
  
    if lives == 0:  # Check if the player ran out of lives
      print("You lose! The word was:", theword)
      guessloop = 1  # End the game loop
  else:
    break

if continuex == 2:
  from subprocess import call
  def open_py_file():
      call(["python", "index.py"])
  open_py_file()
