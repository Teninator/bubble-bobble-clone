# main.py

from app import App
from screens.menu import MenuScreen
from input import build_input_state

WIDTH = 800
HEIGHT = 600

app = App()
app.change_screen(MenuScreen(app))

def update():
    input_state = build_input_state()
    app.update(input_state)

def draw():
    app.draw()

