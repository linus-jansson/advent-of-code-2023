def sumOfGame(game):
    pass

def main(input):
    for game in inp:
        game = game.split(":")
        print(game)
        sumOfGame(game)


if __name__ == "__main__":
    inp = []

    file = open("input.txt", "r")
    inp = file.readlines()
    file.close()

    result = main(inp)