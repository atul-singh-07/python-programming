# 1️⃣ Number Guessing Game 🎮
# Computer picks a random number and the user guesses it.

# Example flow:

# Welcome to Guess Game
# Guess number between 1-100

# Enter guess: 50
# Too high

# Enter guess: 25
# Too low

# Enter guess: 37
# Correct! 🎉
import random
secret_number = random.randint(1,10)

print("Welcome to Guess Game")
print("Guess number between 1-10")

n=int(input("Enter Guess:"))
if(secret_number==n):
    print("Correct!")
elif(secret_number<n):
    print("Too High")
else:
    print("Too Low")


