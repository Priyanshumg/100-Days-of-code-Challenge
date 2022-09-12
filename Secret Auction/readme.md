# Secret Auction
Hello Programmers, Secret Auction is a program which stores data using key and values in python dictionaries <br />
So the dictionary holds keys and values <br />
    **Dict = {User_name : bidding_amount}**
    <br />
So after completion of the Secret Auction, we created a for loop which will iterate through each line and will choose the maximum out of it <br />
## This Specific line of code will check who is having the maximum bidding value and will print that value
```
for person in auction:
  if auction[person] == highest_bid:
    print(f"{person} is the winner of the auction with bidding amount {highest_bid}")
```
<br />
So it's a checker and max key value calculator in this program

## How we took details of User Name and User Bidding Amount 
For this we wrote this line of code which will help in storing user information
```
while True:
  bidding_person = input("What is your name? ")
  bidding_amount = int(input("Bidding Amount : "))
  auction[bidding_person] = bidding_amount
  if input("Is their anyone left? ").lower() == "no":
    break
```
While user does not say "no", The loop wll go on and on
