class App:
    def __init__(self):
        self.screen = None

    def change_screen(self, screen):
        self.screen = screen

    def update(self, input_state):
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
