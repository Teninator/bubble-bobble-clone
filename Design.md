# Design Document — Cavern Refactor

## Overview
This project refactors the original PyGame Zero *Cavern* (Bubble Bobble–style) game to improve structure and maintainability while preserving gameplay behavior exactly. The refactor introduces screen-based state management, centralized input handling with edge detection, and a pause feature.

No gameplay logic, rules, scoring, or timing were changed.

---

## Screen Architecture (State Pattern)

The game uses a screen-based architecture managed by a central `App` object.

### App
- Owns the currently active screen
- Delegates `update()` and `draw()` calls
- Handles screen transitions via `change_screen(screen)`

### Screens
Each screen implements:
- `update(input_state)`
- `draw()`

Implemented screens:
- **MenuScreen**  
  Displays the title screen and transitions to gameplay on SPACE.
- **PlayScreen**  
  Owns the active `Game` instance and handles pause logic.
- **GameOverScreen**  
  Displays the game-over screen and returns to the menu on SPACE.

This removes all global branching on game state and replaces it with explicit screen objects.

---

## Input Handling (Input Snapshot + Edge Detection)

Input is captured once per frame in a centralized `build_input_state()` function.

### InputState
An immutable snapshot containing:
- `left`, `right` — movement
- `jump_pressed` — edge-triggered jump
- `fire_pressed` — edge-triggered orb creation
- `fire_held` — continuous orb blowing
- `pause_pressed` — pause toggle

### Benefits
- No entity accesses `keyboard` directly
- Edge detection is explicit and predictable
- Player logic is easier to test and reason about

---

## Pause Design

Pause is implemented inside `PlayScreen`.

- Toggled using `P`
- While paused:
  - Game simulation is frozen (`Game.update()` not called)
  - Rendering continues
  - A pause overlay is displayed
- Pause is only active during gameplay, not in menu or game-over screens

This avoids introducing a separate pause state while still meeting the requirements.

---

## Summary
This refactor improves separation of concerns, removes hidden global state, and introduces clear architectural boundaries, while maintaining identical gameplay behavior to the original implementation.
