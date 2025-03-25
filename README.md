# Word Guessing Game 🎮

A fun and interactive word guessing game built in Python that challenges players to guess words based on patterns and hints.

## Preview
![Word Guessing Game Preview](src/preview.gif)

## Features
- Interactive command-line interface
- Pattern-based word guessing
- Limited attempts (10 tries)
- Help system for possible letters
- Multiple word patterns and possibilities
- User-friendly game flow

## How It Works
The game uses a JSON file containing word patterns and their possible solutions. Players are given hints about the word's:
- Starting letter
- Ending letter
- Word length

Players have 10 attempts to guess the correct word. They can use the help system to get additional hints about possible letters.


## Code Explanation

### Main Components

1. **Word Pattern Loading**
```python
import json
import random
with open('./src/words.json', 'r') as f:
    data = json.load(f)
data = data["word_patterns"]
```
- The game loads word patterns from a JSON file
- Uses Python's built-in `json` module for data handling
- Random selection of word patterns for variety

2. **Game Loop**
```python
while True:
    print("~"*40) 
    print("To start the game, type 1")
    print("To exit the game, type 0")
    print("~"*40) 
    start = input("Enter your choice: ")
```
- Main game loop with start/exit options
- Clear visual separation using separator lines

3. **Word Guessing Logic**
```python
while max_attempts > 0:
    letters = pattern["pattern"].split("?")
    print("guess the word:start with  ", letters[0], "  and contains  ", letters[-1])
    print("length of the word is : ", len(pattern["pattern"]))
```
- Splits pattern to show first and last letters
- Displays word length as a hint
- Manages remaining attempts

4. **Guess Validation**
```python
if guess.lower() in pattern["words"]:
    print("You guessed the word! in ", max_attempts, " attempts")
else:
    print("Wrong guess!")
    max_attempts -= 1
```
- Case-insensitive word checking
- Attempt counter management
- Win/lose condition handling

## How to Play
1. Run the game using Python: `python main.py`
2. Choose to start (1) or exit (0)
3. Use the hints provided to guess the word
4. Type 'help' for additional letter hints
5. You have 10 attempts to guess correctly

## Technologies Used
- Python 3.x
- JSON for data storage

## Future Improvements
- Add difficulty levels
- Implement scoring system
- Add more word patterns
- Create a GUI version
- Add multiplayer support

## Contributing
Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

