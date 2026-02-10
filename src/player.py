class Player(GravityActor):
    def update(self, input_state):
        super().update(self.health > 0)

        self.fire_timer -= 1
        self.hurt_timer -= 1

        dx = 0
        if input_state.left:
            dx = -1
        elif input_state.right:
            dx = 1

        if dx != 0:
            self.direction_x = dx
            if self.fire_timer < 10:
                self.move(dx, 0, 4)

        if input_state.fire_pressed and self.fire_timer <= 0 and len(game.orbs) < 5:
            x = min(730, max(70, self.x + self.direction_x * 38))
            y = self.y - 35
            self.blowing_orb = Orb((x, y), self.direction_x)
            game.orbs.append(self.blowing_orb)
            game.play_sound("blow", 4)
            self.fire_timer = 20

        if input_state.jump_pressed and self.vel_y == 0 and self.landed:
            self.vel_y = -16
            self.landed = False
            game.play_sound("jump")

        if input_state.fire_held and self.blowing_orb:
            self.blowing_orb.blown_frames = min(120, self.blowing_orb.blown_frames + 4)
        else:
            self.blowing_orb = None
