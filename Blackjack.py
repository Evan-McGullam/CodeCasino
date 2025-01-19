start = 0
aceval = 0
againloop = 0
answerval = 0
exitgame = 3
houseturn = 0
while start == 0:
  print("--------------------------------------------------")
  print("--------------------------------------------------")
  print("Ready to Start? Yes or No?")
  x = input()
  if x.lower() == "yes":
    print("Okay, let's start!")
    print("")
    start = 1
  elif x.lower() == "no":
    print("Come back any time!")
  else:
    print("Please enter a valid input. Only 'Yes' or 'No' are accepted.")
bust = 0
initial = 0
hit = 0
import random
startcard1 = random.randint(1,11)
startcard2 = random.randint(1,11)
housestart1 = random.randint(1,11)
housestart2 = random.randint(1,11)
print("Your starting cards are", startcard1, "and", startcard2,", totalling", startcard1+startcard2)
totalcard = startcard1+startcard2
while aceval == 0:
  if startcard1 == 11 and startcard2 == 11:
    print("You have 2 Aces! Would you like your total to be 12 or 2?")
    y = input()
    if y == "12":
      totalcard = 12
      aceval = 1
    elif y == "2":
      totalcard = 2
      aceval = 1
  elif startcard1 == 1 and startcard2 == 1:
    print("You have 2 Aces! Would you like your total to be 12 or 2?")
    y = input()
    if y == "12":
      totalcard = 12
      aceval = 1
    elif y == "2":
      totalcard = 2
      aceval = 1
  elif startcard1 != 11 or 1 and startcard2 != 11 or 1:
    aceval = 1
  else:
    print("Please input a valid option.")
print("The House's starting cards are", housestart1, "and X, totalling", housestart1, "+ X. Remember the House still has one card face down (X).")
print("Would you like to hit or stand? Remember anything above 21 is a bust.")
initial = 1
continuedhit = 0
newtotalcard = 0
while answerval == 0:
  rehit = input("Hit or Stand?")
  bust = 0
  while bust == 0:
    if rehit.lower() == "hit":
      newtotalcard = newtotalcard + totalcard + random.randint(1,11)
      print("Your new total is",newtotalcard)
      if newtotalcard > 21:
        print("You lose! Total exceeds 21 :(")
        bust = 1
        exitcontloop = 1
        answerval = 1
        break
      elif newtotalcard == 21:
        print("You have 21! Blackjack!")
        continuedhit = 1
        exitcontloop = 1
        bust = 1
        answerval = 1
        houseturn = 1
        break
      while againloop == 0:
        exitcontloop = input("Would you like to hit again or stand?")
        if exitcontloop.lower() == "stand":
          continuedhit = 1
          exitcontloop = 1
          bust = 1
          againloop = 1
          answerval = 1
          houseturn = 1
          break
        elif exitcontloop.lower() == "hit":
            newtotalcard = newtotalcard + random.randint(1,11)
            print("Your new total is",newtotalcard)
            if newtotalcard > 21:
              print("You lose! Total exceeds 21 :(")
              bust = 1
              exitcontloop = 1
              answerval = 1
              againloop = 1
              continuedhit = 1
              break
            elif newtotalcard == 21:
              print("You have 21! Blackjack!")
              bust = 1
              exitcontloop = 1
              againloop = 1
              answerval = 1
              houseturn = 1
              continuedhit = 1
              break
        else:
          print("Please enter a valid input. Only 'Hit' or 'Stand' are accepted.")
    elif startcard1 + startcard2 == 21:
        print("You have 21! Blackjack!")
        answerval = 1
        bust = 1
        houseturn = 1
        break
    elif rehit.lower() == "stand":
        newtotalcard = totalcard
        bust = 1
        answerval = 1
        houseturn = 1
    elif continuedhit ==1:
        bust = 1
        answerval = 1
    else:
      print("Please enter a valid input")
      answerval = 0
      bust = 1
      
ovospecialcard = startcard1 + startcard2
while houseturn == 1:
    print("--------------------------------------------------")
    print("The housetotal is", housestart1+housestart2)
    housetotal = housestart1+housestart2
    if ovospecialcard == 21:
      if housetotal == 21:
        print("House has blackjack! Push.")
        break
      elif housetotal != 21:
        print("You win! asd")
        break
    elif newtotalcard == 21:
      if housetotal == 21:
        print("House has blackjack! Push.")
        break
      elif housetotal != 21:
        print("You win!")
        break
    else:
      while housetotal < 17:
        print("The house has less than 17, so the house will hit.")
        housetotal = housetotal + random.randint(1,11)
        print("The new house total is",housetotal)
      if housetotal == 21 and newtotalcard == 21:
        print("You and the house have 21! It's a draw!")
        bust = 2
        break
      elif housetotal > 21:
        print("The house has busted! You win!")
        bust = 2
        break
      elif housetotal > newtotalcard:
        print("The house has a higher total than you! You lose!")
        bust = 2
        break
      elif housetotal < newtotalcard:
        print("You have a higher total than the house! You win!")
        bust = 2
        break

while exitgame == 3:
  from subprocess import call
  def open_py_file():
      call(["python", "index.py"])
  open_py_file()
  exitgame = 4
