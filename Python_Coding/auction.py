print("Welcome to the secret auction program.")

dict = {}

is_True = True

while is_True:

  name = input("What is your name:")
  bid = int(input("What's your bid?: $"))

  dict[name] = bid



  adding_bidder = input("Are there any other bidders? (yes/no)")

  if adding_bidder == "yes":
    continue

  elif adding_bidder == "no":

    highest_bidder = max(dict, key = dict.get)

    print(f"The winner is {highest_bidder} with a bid of ${dict[highest_bidder]}")

    is_True = False