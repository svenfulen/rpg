import pygame
import items


class Player:
    def __init__(self):
        # player textures
        self.tx_face_down = pygame.image.load("assets/graphics/chars/base/down.png")
        self.tx_face_left = pygame.image.load("assets/graphics/chars/base/left.png")
        self.tx_face_up = pygame.image.load("assets/graphics/chars/base/up.png")
        self.tx_face_right = pygame.image.load("assets/graphics/chars/base/right.png")

        # Walk animations
        self.tx_walk_down = [pygame.image.load("assets/graphics/chars/base/down_walk/dw_1.png"),
                             pygame.image.load("assets/graphics/chars/base/down_walk/dw_2.png"),
                             pygame.image.load("assets/graphics/chars/base/down_walk/dw_3.png"),
                             pygame.image.load("assets/graphics/chars/base/down_walk/dw_4.png")]

        self.tx_walk_left = [pygame.image.load("assets/graphics/chars/base/left_walk/lw_1.png"),
                             pygame.image.load("assets/graphics/chars/base/left_walk/lw_2.png"),
                             pygame.image.load("assets/graphics/chars/base/left_walk/lw_3.png"),
                             pygame.image.load("assets/graphics/chars/base/left_walk/lw_4.png")]

        self.tx_walk_up = [pygame.image.load("assets/graphics/chars/base/up_walk/uw_1.png"),
                           pygame.image.load("assets/graphics/chars/base/up_walk/uw_2.png"),
                           pygame.image.load("assets/graphics/chars/base/up_walk/uw_3.png"),
                           pygame.image.load("assets/graphics/chars/base/up_walk/uw_4.png")]

        self.tx_walk_right = [pygame.image.load("assets/graphics/chars/base/right_walk/rw_1.png"),
                              pygame.image.load("assets/graphics/chars/base/right_walk/rw_2.png"),
                              pygame.image.load("assets/graphics/chars/base/right_walk/rw_3.png"),
                              pygame.image.load("assets/graphics/chars/base/right_walk/rw_4.png")]

        # Stab attack animations
        self.tx_stab_down = pygame.image.load("assets/graphics/chars/base/stab/down_hit.png")
        self.tx_stab_left = pygame.image.load("assets/graphics/chars/base/stab/left_hit.png")
        self.tx_stab_up = pygame.image.load("assets/graphics/chars/base/stab/up_hit.png")
        self.tx_stab_right = pygame.image.load("assets/graphics/chars/base/stab/right_hit.png")

        # player equipment data
        self.weapon_equipped = True
        self.weapon = items.Weapon("test_sword")
        self.weapon_damage = 1

        # player location/velocity/state info
        self.x_pos = 50
        self.y_pos = 50
        self.x_tile = int(self.x_pos / 32)  # These are estimations of the tile the player will be on
        self.y_tile = int(self.y_pos / 32)
        self.attacking = False
        self.walk_speed = 3
        self.walking = False  # If the player is currently moving
        self.walkCount = 0
        self.faceDirection = "D"  # U D L R for each direction
        self.can_move_up = True
        self.can_move_down = True
        self.can_move_left = True
        self.can_move_right = True

        # player collision data
        self.hit_box = ((self.x_pos + 10), (self.y_pos + 3), 12, 28)
        self.T_R = ((self.x_pos + 10), (self.y_pos + 3), 12, 1)
        self.B_R = ((self.x_pos + 10), (self.y_pos + 30), 12, 1)
        self.L_R = ((self.x_pos + 10), (self.y_pos + 4), 1, 26)
        self.R_R = ((self.x_pos + 21), (self.y_pos + 4), 1, 26)
        self.top_rect = pygame.Rect(self.T_R)
        self.bottom_rect = pygame.Rect(self.B_R)
        self.left_rect = pygame.Rect(self.L_R)
        self.right_rect = pygame.Rect(self.R_R)
        self.rect = pygame.Rect(self.hit_box)

        self.stab_rect_up = pygame.Rect(((self.x_pos + 10), (self.y_pos + 3), 12, 1))
        self.stab_rect_down = pygame.Rect(((self.x_pos + 10), (self.y_pos + 30), 12, 1))
        self.stab_rect_left = pygame.Rect((self.x_pos, (self.y_pos + 20), 10, 4))
        self.stab_rect_right = pygame.Rect(((self.x_pos + 21), (self.y_pos + 20), 10, 4))

        self.weapon_rect = pygame.Rect(0, 0, 0, 0)

    def spawn(self, surface_to_draw, x, y):  # starts the player off at a certain position
        surface_to_draw.blit(self.tx_face_down, (self.x_pos, self.y_pos))  # spawn the player facing down
        self.x_pos = x
        self.y_pos = y

    def draw(self, surface_to_draw, timer):  # draws the player every frame
        self.hit_box = ((self.x_pos + 10), (self.y_pos + 3), 12, 28)
        self.T_R = ((self.x_pos + 10), (self.y_pos + 3), 12, 1)
        self.B_R = ((self.x_pos + 10), (self.y_pos + 30), 12, 1)
        self.L_R = ((self.x_pos + 10), (self.y_pos + 4), 1, 26)
        self.R_R = ((self.x_pos + 21), (self.y_pos + 4), 1, 26)
        self.rect = pygame.Rect(self.hit_box)
        self.top_rect = pygame.Rect(self.T_R)
        self.bottom_rect = pygame.Rect(self.B_R)
        self.left_rect = pygame.Rect(self.L_R)
        self.right_rect = pygame.Rect(self.R_R)
        self.stab_rect_up = pygame.Rect(((self.x_pos + 10), (self.y_pos + 3), 12, 1))
        self.stab_rect_down = pygame.Rect(((self.x_pos + 10), (self.y_pos + 30), 12, 1))
        self.stab_rect_left = pygame.Rect((self.x_pos, (self.y_pos + 20), 10, 4))
        self.stab_rect_right = pygame.Rect(((self.x_pos + 21), (self.y_pos + 20), 10, 4))

        if self.walkCount + 1 >= 16:
            self.walkCount = 0
        # Logic for animations / drawing
        if self.faceDirection == "D":
            if self.attacking:
                time_since_enter = pygame.time.get_ticks() - timer
                surface_to_draw.blit(self.tx_stab_down, (self.x_pos, self.y_pos))
                self.weapon_rect = self.stab_rect_down
                if self.weapon_equipped:
                    surface_to_draw.blit(self.weapon.down_attack_texture, (self.x_pos, self.y_pos))
                if time_since_enter >= 100:
                    self.attacking = False
                    self.weapon_rect = (0, 0, 0, 0)
            else:
                if self.walking:
                    surface_to_draw.blit(self.tx_walk_down[self.walkCount//4], (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.walk_down_texture[self.walkCount//4], (self.x_pos, self.y_pos))
                    self.walkCount += 1
                if not self.walking:
                    surface_to_draw.blit(self.tx_face_down, (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.face_down_texture, (self.x_pos, self.y_pos))

        if self.faceDirection == "L":
            if self.attacking:
                time_since_enter = pygame.time.get_ticks() - timer
                surface_to_draw.blit(self.tx_stab_left, (self.x_pos, self.y_pos))
                self.weapon_rect = self.stab_rect_left
                if self.weapon_equipped:
                    surface_to_draw.blit(self.weapon.left_attack_texture, (self.x_pos, self.y_pos))
                if time_since_enter >= 100:
                    self.attacking = False
                    self.weapon_rect = (0, 0, 0, 0)
            else:
                if self.walking:
                    surface_to_draw.blit(self.tx_walk_left[self.walkCount//4], (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.walk_left_texture[self.walkCount//4], (self.x_pos, self.y_pos))
                    self.walkCount += 1
                if not self.walking:
                    surface_to_draw.blit(self.tx_face_left, (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.face_left_texture, (self.x_pos, self.y_pos))

        if self.faceDirection == "U":
            if self.attacking:
                time_since_enter = pygame.time.get_ticks() - timer
                surface_to_draw.blit(self.tx_stab_up, (self.x_pos, self.y_pos))
                self.weapon_rect = self.stab_rect_up
                if self.weapon_equipped:
                    surface_to_draw.blit(self.weapon.up_attack_texture, (self.x_pos, self.y_pos))
                if time_since_enter >= 100:
                    self.attacking = False
                    self.weapon_rect = (0, 0, 0, 0)
            else:
                if self.walking:
                    surface_to_draw.blit(self.tx_walk_up[self.walkCount//4], (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.walk_up_texture[self.walkCount//4], (self.x_pos, self.y_pos))
                    self.walkCount += 1
                if not self.walking:
                    surface_to_draw.blit(self.tx_face_up, (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.face_up_texture, (self.x_pos, self.y_pos))

        if self.faceDirection == "R":
            if self.attacking:
                time_since_enter = pygame.time.get_ticks() - timer
                surface_to_draw.blit(self.tx_stab_right, (self.x_pos, self.y_pos))
                self.weapon_rect = self.stab_rect_right
                if self.weapon_equipped:
                    surface_to_draw.blit(self.weapon.right_attack_texture, (self.x_pos, self.y_pos))
                if time_since_enter >= 100:
                    self.attacking = False
                    self.weapon_rect = (0, 0, 0, 0)
            else:
                if self.walking:
                    surface_to_draw.blit(self.tx_walk_right[self.walkCount//4], (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.walk_right_texture[self.walkCount//4], (self.x_pos, self.y_pos))
                    self.walkCount += 1
                if not self.walking:
                    surface_to_draw.blit(self.tx_face_right, (self.x_pos, self.y_pos))
                    if self.weapon_equipped:
                        surface_to_draw.blit(self.weapon.face_right_texture, (self.x_pos, self.y_pos))

        # COLLISIONS DEBUG #

        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.hit_box, 1)
        # pygame.draw.rect(surface_to_draw, (0, 0, 255), self.top_rect, 1)
        # pygame.draw.rect(surface_to_draw, (255, 165, 0), self.bottom_rect, 1)
        # pygame.draw.rect(surface_to_draw, (255, 0, 0), self.left_rect, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.right_rect, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.stab_rect_up, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.stab_rect_down, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.stab_rect_left, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.stab_rect_right, 1)
        # pygame.draw.rect(surface_to_draw, (255, 0, 0), self.weapon_rect, 1)

        # COLLISIONS DEBUG #

    def move_up(self):
        self.y_pos = self.y_pos - self.walk_speed
        self.y_tile = int(self.y_pos / 32)

    def move_down(self):
        self.y_pos = self.y_pos + self.walk_speed
        self.y_tile = int(self.y_pos / 32)

    def move_left(self):
        self.x_pos = self.x_pos - self.walk_speed
        self.x_tile = int(self.x_pos / 32)

    def move_right(self):
        self.x_pos = self.x_pos + self.walk_speed
        self.x_tile = int(self.x_pos / 32)

    # def attack(self, surface_to_draw):
