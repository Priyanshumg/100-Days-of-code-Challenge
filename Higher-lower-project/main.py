from art import logo, vs
from game_data import data
from random import choice

def format(account):
  """takes the account to printable format"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, {description},from {country}"

def check_ans(guess, follower_a, follower_b):
  """take the user guess and follower returns if it's right"""
  if follower_a > follower_b:
    return guess == "a"
  else:
    return guess == "b"

# Display Art
print(logo)
game_should_continue = True
account_b = choice(data)
score = 0

# Make the game repeatable
while game_should_continue is True:
  # Making account at position B become the next account at position A.
  # Generate a random account from the game data.
  account_a = account_b
  account_b = choice(data)
  while account_a == account_b:
    account_b = choice(data)
  
  # format the account to printable format
  print(f"Compare A : {format(account_a)}")
  print(vs)
  print(f"Against B : {format(account_b)}")
  
  # Ask a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # check if user is correct or not
  ## Get follower count for each account
  followers_account_a = account_a["follower_count"]
  followers_account_b = account_b["follower_count"]
  
  ## Use if statement if user is correct 
  is_correct = check_ans(guess, followers_account_a, followers_account_b)
  
  # give user feedback of their guess
  # score keeping
  if is_correct:
    score += 1
    print(f"You are right!, your score is {score}")
  else:
    print(f"Sorry, That's wrong, Final Score : {score}")
    game_should_continue = False
