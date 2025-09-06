import random

class Ludo:
    def __init__(self):
        self.players = []
        self.board = []
        self.dice = Dice()

    def add_player(self, player):
        self.players.append(player)

    def play(self):
        if not self.players:
            print("No players have been added to the game.")
            return
        
        for player in self.players:
            dice_roll = self.dice.roll()
            player.move(dice_roll)

            if player.is_winner():
                print(f"Player {player.name} wins!")
                break

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, dice_roll):
        self.position += dice_roll

