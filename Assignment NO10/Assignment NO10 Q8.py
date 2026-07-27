class Player:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score += points

    def level_up(self):
        self.level += 1

    def show_progress(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)


player = Player("Shashwat", 100, 1)

player.show_progress()

player.increase_score(50)
player.level_up()

player.increase_score(100)
player.level_up()

player.show_progress()