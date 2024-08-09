import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty.Type 'easy' or 'hard': ")

if difficulty == "easy":
  player_life = 8

elif difficulty == "hard":
  player_life = 5


chosen_number = random.randint(1, 101)


while True:
  if player_life > 0:
    print(f"You have {player_life} attemps remaining to guess the number.")

    
    guess = int(input("Make a guess:"))

    if chosen_number > guess:
      print("Too low value.\nMake another guess.")
      player_life = player_life - 1
      
      
    elif chosen_number < guess:
      print("Too high.\nMake another guess.")
      player_life = player_life - 1
  
    elif chosen_number == guess:
      print("You've won.Congratulations..!")
      print(f"{guess}")
      break

  elif player_life == 0:
    print("You lose.")
    print(f"{guess}")
    break