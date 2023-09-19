class GuessCounter:
    def __init__(self) -> None:
        self.current_guesses = 6

    def update_guesses(self) -> int:
        self.current_guesses -= 1
        return self.current_guesses
    
    def __str__(self) -> str:
        if self.current_guesses == 0:
            return f'You have no more guesses - Game Over'
        return f'You have {self.current_guesses} guesses'