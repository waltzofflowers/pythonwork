#from replit import clear
from game_data import data
#from art import logo, vs
import random

decision = ""

score = 0

a = random.randint(0, len(data) - 1)

while True:
  #clear()
  #print(logo)
  if score >= 1:
    print(f"You are right! Current score: {score}")
  
  b = random.randint(0, len(data) - 1)

  while b == a:
    b = random.randint(0, len(data) - 1)
  
  a_name = data[a]["name"]
  a_follower = data[a]["follower_count"]
  a_description = data[a]["description"]

  b_name = data[b]["name"]
  b_follower = data[b]["follower_count"]
  b_description = data[b]["description"]

  print(f"Compare A: {a_name}, {a_description}")
  #print(vs)
  print(f"Compare B: {b_name}, {b_description}")

  decision = input("Who has more followers? Type 'A' or 'B':").lower()

  if decision == "a" and a_follower > b_follower:
    score = score + 1
    a = b
    
  elif decision == "b" and b_follower > a_follower:
    score = score + 1
    a = b
    
  else:
    #clear()
    #print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    break
