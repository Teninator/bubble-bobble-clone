from screens.play import PlayScreen
from game import Game

class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(None)

    def update(self, input_state):
        self.game.update(None)
        if input_state.fire_pressed:
            self.app.change_screen(PlayScreen(self.app))

    def draw(self):
        self.game.draw()
        screen.blit("title", (0, 0))

        anim = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim), (130, 280))
