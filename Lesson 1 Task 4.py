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
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
            winner = self.round_winner(answer1, answer2)
            if winner == 1:
                self.wins1 += 1
                print("player 1 won")
            elif winner == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass  # it's a tie
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return None


class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        self.vowels = 'aeiouAEIOU'

    def round_winner(self, player1_word: str, player2_word: str):
        counts1 = sum(1 for ch in player1_word if ch in self.vowels)
        counts2 = sum(1 for ch in player2_word if ch in self.vowels)
        if counts1 > counts2:
            return 1
        elif counts1 < counts2:
            return 2
        else:
            return None


class RockPaperScissors(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if (player1_word == "rock" and player2_word == "scissors" or
                player1_word == "scissors" and player2_word == "paper" or
                player1_word == "paper" and player2_word == "rock"):
            return 1
        elif (player2_word == "rock" and player1_word == "scissors" or
              player2_word == "scissors" and player1_word == "paper" or
              player2_word == "paper" and player1_word == "rock"):
            return 2
        else:
            return None


p = RockPaperScissors(4)
p.play()

p = MostVowels(3)
p.play()

p = LongestWord(3)
p.play()










