import pygame


class Player:
    def __init__(self):
        # player textures
        self.tx_face_down = pygame.image.load("E:/game/assets/graphics/chars/test_bob/bob_south.png")
        self.tx_face_left = pygame.image.load("E:/game/assets/graphics/chars/test_bob/bob_left.png")
        self.tx_face_up = pygame.image.load("E:/game/assets/graphics/chars/test_bob/bob_north.png")
        self.tx_face_right = pygame.image.load("E:/game/assets/graphics/chars/test_bob/bob_right.png")

        # player location/velocity/state info
        self.x_pos = 50
        self.y_pos = 50
        self.walk_speed = 3
        self.walking = False  # If the player is currently moving
        self.faceDirection = "D"  # U D L R for each direction
        self.can_move_up = True
        self.can_move_down = True
        self.can_move_left = True
        self.can_move_right = True

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

    def spawn(self, surface_to_draw, x, y):  # starts the player off at a certain position
        # TODO: player animations and graphics
        surface_to_draw.blit(self.tx_face_down, (self.x_pos, self.y_pos))  # spawn the player facing down
        self.x_pos = x
        self.y_pos = y

    def draw(self, surface_to_draw):  # draws the player every frame
        # TODO: player animations and graphics
        if self.faceDirection == "D":
            if not self.walking:
                surface_to_draw.blit(self.tx_face_down, (self.x_pos, self.y_pos))
        if self.faceDirection == "L":
            if not self.walking:
                surface_to_draw.blit(self.tx_face_left, (self.x_pos, self.y_pos))
        if self.faceDirection == "U":
            if not self.walking:
                surface_to_draw.blit(self.tx_face_up, (self.x_pos, self.y_pos))
        if self.faceDirection == "R":
            if not self.walking:
                surface_to_draw.blit(self.tx_face_right, (self.x_pos, self.y_pos))
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
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.hit_box, 1)
        # pygame.draw.rect(surface_to_draw, (0, 0, 255), self.top_rect, 1)
        # pygame.draw.rect(surface_to_draw, (255, 165, 0), self.bottom_rect, 1)
        # pygame.draw.rect(surface_to_draw, (255, 0, 0), self.left_rect, 1)
        # pygame.draw.rect(surface_to_draw, (0, 255, 0), self.right_rect, 1)

    def move_up(self):
        # walking = True  (need to set these statements to false when not walking)
        self.y_pos = self.y_pos - self.walk_speed

    def move_down(self):
        # walking = True
        self.y_pos = self.y_pos + self.walk_speed

    def move_left(self):
        # walking = True
        self.x_pos = self.x_pos - self.walk_speed

    def move_right(self):
        # walking = True
        self.x_pos = self.x_pos + self.walk_speed
