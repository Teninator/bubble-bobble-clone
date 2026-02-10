from player import Player

class Game:
    def __init__(self):
        self.is_game_over = False
        self.player = Player()

        # ✅ REQUIRED initializations
        self.timer = 0
        self.fruits = []
        self.bolts = []
        self.enemies = []
        self.pops = []
        self.orbs = []

    def update(self, input_state):
        self.timer += 1

        for obj in (
            self.fruits
            + self.bolts
            + self.enemies
            + self.pops
            + [self.player]
            + self.orbs
        ):
            if obj:
                if obj == self.player:
                    obj.update(input_state)
                else:
                    obj.update()

    def draw(self):
        screen.clear()
        self.player.draw()
