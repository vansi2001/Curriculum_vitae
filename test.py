import random
# Generate a random number between 1-100
target_number = random.randint(1, 100)
guess_position = random.randint(0, len(str(target_number)) - 1)
target_digit = str(target_number)[guess_position]

print(f"I'm thinking of a {len(str(target_number))}-digit number: {target_number}")
print(f"Can you guess which digit is in position {guess_position + 1}?")

user_guess = input("Enter your guess: ")

if user_guess == target_digit:
    print("Correct! You guessed the right digit!")
else:
    print(f"Wrong! The digit in position {guess_position + 1} was {target_digit}")
