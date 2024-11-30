class Game():
    def __init__(self, textstr: str) -> None: # Initialises a game
        if type(textstr) is None:
            raise TypeError("Game must be initialised with a text string")
        # normalise type
        self.game_id = int((x := (textstr.split(":")))[0][5:])
        self.games = x[1].split(";")
        self.game_count = len(self.games)
        self.game_list = [Subset(x) for x in self.games]

    def isLegalGame(self, legal) -> bool:
        return all([subset < legal for subset in self.game_list])
    
    def __str__(self):
        return str(self.games)

class Subset():
    def __init__(self, gamestr: str) -> None:
        self.data = {
            'red' : 0,
            'green' : 0,
            'blue' : 0
        }

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

def main():
    data = [x.strip() for x in open("in02.txt", 'r').readlines()]
    legalGame = Subset(" 14 blue, 12 red, 13 green")
    id_sum = 0

    for line in data:
        currentGame = Game(line)
        if currentGame.isLegalGame(legalGame):
            id_sum += currentGame.game_id

    print(id_sum)


if __name__ == "__main__":
    main()

    
    


