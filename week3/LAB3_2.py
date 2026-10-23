# --- Lab 3.2 Part 1: Countdown Timer ---
start = int(input("Enter starting number for countdown: "))
while start >= 0:
    print(start)
    start = start-1
print("Blast off!")



## --- Lab 3.2 Part 2: Simple Guessing Game ---
secret_number = 42

while True:
    guess = int(input("Guess the number: "))
   
    if (guess < secret_number):
        print(f"{guess} is too low! Try again.")
    elif (guess > secret_number):
        print(f"{guess} is too high! Try again.")
    else:
        print("Congratulations! You guessed it!")
        break