import json
import random
with open('./src/words.json', 'r') as f:
    data = json.load(f)

data = data["word_patterns"]
while True:
    print("~"*40) 
    print("To start the game, type 1")
    print("To exit the game, type 0")
    print("~"*40) 
    start = input("Enter your choice: ")
    print("~"*40) 
    if start == "1":
        print("Hi, I'm a word guessing game. I'll think of a word and you have to guess it.")
        print("~"*40) 
        max_attempts = 10
        print(f"You have {max_attempts} attempts to guess the word.")
        print("for help, type help it gives you possible letters to guess")
        print("~"*40) 
        pattern = random.choice(data)

        while max_attempts > 0:
            letters = pattern["pattern"].split("?")
            print("guess the word:start with  ", letters[0], "  and contains  ", letters[-1])
            print("length of the word is : ", len(pattern["pattern"]))
            print("~"*40) 
            guess = input("Enter your guess: ")
            print("~"*40) 
            if guess.lower() in pattern["words"]:
                print("You guessed the word! in ", max_attempts, " attempts")
                print("~"*40) 
                break
            else:
                print("Wrong guess!")
                max_attempts -= 1
                if max_attempts == 0:
                    print("You ran out of attempts! The possible words were:")
                    print(pattern["words"])
                    print("~"*40) 
                    break
    elif start == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input!")
        continue
