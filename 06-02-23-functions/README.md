# Functions

This exercise is to help you familiarize yourself with variables and objects:
* how scoping works, and which names are visible from where
* how objects are passed to and returned from functions
* the differences between assignment and mutation

## Your Mission

There are three programs you should write, in increasing difficulty.
* The classic number guessing game. The computer picks a number between 1 and 100, and asks you to guess. It tells you if you were too high or too low, and gives you six chances to guess.
* Hangman. The computer picks a word from a selection it knows, shows you the blanks, and asks you to guess. Every successful guess fills in those blanks. Every failed guess draws a new piece of the hangman. You have six chances to win.
* Wordle. The computer picks a five-letter word from a selection. You have six chances to guess it. After every guess it prints your guess again; every correct letter is in green, and every letter which is in the word but in the wrong position is in yellow.

"Wait" I hear you cry! "We've already written those! This sounds very easy for a Dojo of Doom!!"

...

...

...you didn't think it would be that easy, did you? :)

## The Catch

This exercise is to help you understand how data flows into, through, and out of functions. Therefore, you will need to use lots of functions in your program. To... "encourage" you to do this, you will need to write your program according to the following rules. 

### The Rules

* The global scope of your program can only contain:
  * `import` directives
  * function defintions
  * an import guard; i.e. the bottom of the file should say:
  ```python
  if __name__ == '__main__':
    main()
  ```
  That's _it_. Your import guard calls a function called `main`, and that function has to arrange everything else.
* Each function body can contain no more than five lines.
  * The function signature, i.e. `def myfunc():` does not count towards this limit.
 
