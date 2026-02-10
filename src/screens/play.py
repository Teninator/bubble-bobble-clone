from game import Game
from screens.game_over import GameOverScreen
from player import Player

class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player())
        self.paused = False

    def update(self, input_state):
        if input_state.pause_pressed:
            self.paused = not self.paused

        if self.paused:
            return

        self.game.update(input_state)

        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(GameOverScreen(self.app, self.game))

    def draw(self):
        self.game.draw()
        draw_status()

        if self.paused:
            screen.draw.text("PAUSED", center=(400, 240), fontsize=60)
