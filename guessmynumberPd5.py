
'''
document
'''
import random
secret = random.randint (1,99)
guess = 0
tries = 0
print("can you guess my number")
print("My number is an integer between 1 and 99")
while guess != secret and tries < 6:
    print("what is your guess ?")
    guess - int(input())
    if guess < secret :
        print ("Too Low")
    elif guess > secret :
        print("Too High!")
    tries = tries + 1
if guess == secret :
    print("You got it! bravoooo!")
else :
    print("No more guesses! Try again")
    print("The secert number was : ", secret)



