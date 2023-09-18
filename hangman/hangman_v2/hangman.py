class Hangman:
    def __init__(self, guesses: int) -> None:
        self.guesses = guesses
        self.hangman = self.get_hangman()
        self.current_hangman = self.get_current_hangman()

    def get_hangman(self) -> 'list[str]':
        if self.guesses == 6:
            return self.hangman_6()
        elif self.guesses == 5:
            return self.hangman_5()
        elif self.guesses == 4:
            return self.hangman_4()
        elif self.guesses == 3:
            return self.hangman_3()
        elif self.guesses == 2:
            return self.hangman_2()
        elif self.guesses == 1:
            return self.hangman_1()
        else:
            return self.hangman_0()

    def hangman_6(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|",
            "|",
            "|",
            "|",
            "|________"
        ]
    
    def hangman_5(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|",
            "|",
            "|",
            "|________"
        ]

    def hangman_4(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|      |",
            "|      |",
            "|",
            "|________"
        ]

    def hangman_3(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|     \|",
            "|      |",
            "|",
            "|________"
        ]
    
    def hangman_2(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|     \|/",
            "|      |",
            "|",
            "|________"
        ]
    
    def hangman_1(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|     \|/",
            "|      |",
            "|     /  ",
            "|________"
        ]
    
    def hangman_0(self) -> 'list[str]':
        return [
            "_________",
            "|      |",
            "|      O",
            "|     \|/",
            "|      |",
            "|     / \ ",
            "|________"
        ]
    
    def get_current_hangman(self) -> str:
        hangman = '\n'.join(self.hangman)
        return hangman

    def __str__(self) -> str:
        return f'{self.current_hangman}'
