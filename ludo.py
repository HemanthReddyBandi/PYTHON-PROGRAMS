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
        
        while True:
            for player in self.players:
                input(f"{player.name}, press Enter to roll the dice...")
                dice_roll = self.dice.roll()
                player.move(dice_roll)
                print(f"{player.name} rolled a {dice_roll} and moved to position {player.position}.")

                if player.is_winner():
                    print(f"Player {player.name} wins!")
                    return

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, dice_roll):
        self.position += dice_roll

    def is_winner(self):
        return self.position >= 100

2class Dice:
    def roll(self):
        return random.randint(1, 6)

if __name__ == "__main__":
    game = Ludo()
    num_players = int(input("Enter the number of players: "))
    for _ in range(num_players):
        name = input("Enter player name: ")
        game.add_player(Player(name))
    game.play()
