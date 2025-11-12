# Welcome to Wordl-ish!

Wordl-ish is a game that is a spin-off from the famous Wordle. This game will be a bit more difficult as you will get fewer clues than you would with Wordle.

## How to play:
 - Player 1 will choose a 4 letter word
 - Player 2 has to try and guess the word, everytime they guess a word, Player 1 will respond with the number of letters in the correct position.
 - The game will keep going until Player 2 guesses the correct word.

### Requirements:

- Player 1 will be able to enter a 4 letter word 
    - The word must not include any other characters other than letters
    - The word must equal to 4 letters long
    - Has to be a real word - maybe check against a dictionary (a later rule maybe)
    - Player will hit submit
- Player 2 can enter a 4 letter word
    - Sames rules apply as about, so maybe we create a enter_word component?
- Player 1 responds with the number of characters in the correct position
- Player 2 guesses again
- We keep repeating this cycle until Player 1 responds with 4.

- Once this is built, I can build the point-system
    - Each guess adds 1 point to the counter
    - The final number of guess = the amount of points
    - Aim of the game is to have the least amount of points

- I'll then build in the ability to check if each word entered is a verified word in the dictionary.

- Once the point-system is built, I'll build a play vs computer mode
    - The computer will choose a random word 
    - The Player will always be the one guessing