secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count+1
    if guess == (secret_number):
        print("Correct! You won!")
        break
else:
    print("Sorry you have failed!")
