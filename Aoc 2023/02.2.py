class Game():
    def __init__(self, textstr: str) -> None: # Initialises a game
        if type(textstr) is None:
            raise TypeError("Game must be initialised with a text string")
        # normalise type
        self.game_id = int((x := (textstr.split(":")))[0][5:])
        self.games = x[1].split(";")
        self.game_count = len(self.games)
        self.game_list = [Subset(x) for x in self.games]
        self.minimalgame = self.__getMinimalGame(self.game_list)

    def isLegalGame(self, legal) -> bool:
        return all([subset < legal for subset in self.game_list])
    
    def __str__(self):
        return str(self.games)
    
    def __getMinimalGame(self, game_list):
        min_game = Subset()
        min_game.data['red'] = max([x.data['red'] for x in game_list])
        min_game.data['green'] = max([x.data['green'] for x in game_list])
        min_game.data['blue'] = max([x.data['blue'] for x in game_list])
        return min_game



class Subset():
    def __init__(self, gamestr: str = None) -> None:
        self.data = {
            'red' : 0,
            'green' : 0,
            'blue' : 0
        }

        if gamestr is not None:
            for x in [x.strip().split() for x in gamestr.split(',')]:
                self.data[x[1]] += int(x[0])

    def __lt__(self, obj2: object) -> bool:
        return all([
            self.data['red'] <= obj2.data['red'],
            self.data['green'] <= obj2.data['green'],
            self.data['blue'] <= obj2.data['blue'],
        ])

    def __str__(self):
        return f"r:{self.data['red']},g:{self.data['green']},b:{self.data['blue']}"
    
    def getPower(self) -> int:
        return self.data['red'] * self.data['green'] * self.data['blue']

def main():
    data = [x.strip() for x in open("in02.txt", 'r').readlines()]
    power_sum = 0
    for line in data:
        currentGame = Game(line)
        power_sum += currentGame.minimalgame.getPower()
    
    print(power_sum)
        


if __name__ == "__main__":
    main()

    
    


