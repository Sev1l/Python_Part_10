## Class Hierarchies
# Task 4 (Word game)


import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        self.player1_word = player1_word
        self.player2_word = player2_word
        if len(self.player1_word) > len(self.player2_word):
            return 1
        elif len(self.player1_word) < len(self.player2_word):
            return 2
        else:
            return None


    def play(self):
        super().play()


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        self.vowels = 'aeiouAEIOU'

    def round_winner(self, player1_word: str, player2_word: str):
        self.player1_word = player1_word
        self.player2_word = player2_word
        counts1 = 0
        counts2 = 0
        for i in self.player1_word:
            for j in self.vowels:
                if i == j:
                    counts1 += 1
        for i in self.player2_word:
            for j in self.vowels:
                if i == j:
                    counts2 += 1
        if counts1 > counts2:
            return 1
        elif counts1 < counts2:
            return 2
        else:
            return None


    def play(self):
        super().play()

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        

    def round_winner(self, player1_word: str, player2_word: str):
        self.player1_word = player1_word
        self.player2_word = player2_word
        
        if (self.player1_word == "rock" and self.player2_word == "scissors" or
            self.player1_word == "scissors" and self.player2_word == "paper" or
            self.player1_word == "paper" and self.player2_word == "rock"):
            return 1
        elif (self.player2_word == "rock" and self.player1_word == "scissors" or
              self.player2_word == "scissors" and self.player1_word == "paper" or
              self.player2_word == "paper" and self.player1_word == "rock"):
            return 2

        else:
            pass


    def play(self):
        super().play()
    

p = RockPaperScissors(4)
p.play()



p = MostVowels(3)
p.play()












