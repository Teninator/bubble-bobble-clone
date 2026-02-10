# input.py

from dataclasses import dataclass

@dataclass
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool


_prev = {"space": False, "p": False}

def build_input_state():
    global _prev

    space = keyboard.space
    p = keyboard.p

    # inputs
    state = InputState(
        left=keyboard.left,
        right=keyboard.right,
        jump_pressed=keyboard.up and not _prev["space"],
        fire_pressed=space and not _prev["space"],
        fire_held=space,
        pause_pressed=p and not _prev["p"],
    )

    _prev["space"] = space
    _prev["p"] = p
    return state

