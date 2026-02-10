from screens.menu import MenuScreen

class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state):
        if input_state.fire_pressed:
            self.app.change_screen(MenuScreen(self.app))

    def draw(self):
        self.game.draw()
        draw_status()
        screen.blit("over", (0, 0))
