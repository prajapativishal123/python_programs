import random

l=[]
user=[]

a=random.randint(1,21)


while True:
    b=int(input("enter a number between 1 to 20 : "))
    if a==b:
        print("you guessed right.")
        break
    elif a>b:
        print("you guessed small number.")
    else:
        print("you guessed large number.")
