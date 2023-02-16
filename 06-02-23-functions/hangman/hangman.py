'''
    Challenge:
    The computer picks a word from a selection it knows, shows you the blanks,
    and asks you to guess. Every successful guess fills in those blanks.
    Every failed guess draws a new piece of the hangman. You have six chances to win.

    Problem Steps:
    1. Computer picks a random word from a selection
    2. Give the player the rules to play the game (including that they have 6 chances to guess)
    3. Show player the blanks for each letter of the chosen word
    4. Ask the player to guess a letter
    5. Check if the guessed letter is in the word
    6. If it is, fill in those blanks
    7. Repeat from step 4
    8. If no match, draw a piece of the hangman (decreasing the count by 1)
    9. Repeat from step 4
    10. If all the letters are filled, player wins
    11. Check if player wants to play again - Print 'Would you like to play again? y/n '
    12. If 'y' return to step 1 and set number of guesses back to 6
    13. If 'n' exit()
    14. When guesses == 0, hangman is complete - print 'Too bad, you've run out of guesses'
    15. Return to step 11
'''