import random
number = random.randint(1,100)
guess = 0


while guess != number:

    guess = int(input("enter guess :"))

    if (guess > number) :
        print("guess smaller")
    elif (guess < number) :
        print("guess bigger")

else :
    print("YOU WON!")              