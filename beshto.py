import random

a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))

guess=int(input("Your Guess"))

x=random.randint(a,b)
print(x)

count=5


while count>0:
    guess=int(input("Your Guess"))
    if guess==x:
        print("you won")
        break
    elif guess>x:
        print("the no is smaller than your guess")
        
    elif guess<x:
        print("the no is bigger than your guess")
    else:
        print("Try again")
    count-=1
    
if count==0:
    print("you lost")