import pygame


class Camera:
    def __init__(self, window_x, window_y):
        self.zoom = 3
        self.size = ((window_x * self.zoom), (window_y * self.zoom))
        self.camera = pygame.Surface(self.size)
        # self.rect = ()

    def zoom_in(self, surf, win, player_obj):
        pygame.transform.scale(surf, self.size, self.camera)
        win.blit(self.camera, (-player_obj.x_pos, -player_obj.y_pos))


'''
CAMERA_X_POS = ((-player.x_pos) * CAMERA_ZOOM) + 300
    CAMERA_Y_POS = ((-player.y_pos) * CAMERA_ZOOM) + 250
    pygame.transform.scale(world, CAMERA_SIZE, camera)  # scales up the world 
    camera = pygame.Surface(CAMERA_SIZE)
CAMERA_SIZE = ((WINDOW_X * CAMERA_ZOOM), (WINDOW_Y * CAMERA_ZOOM))
CAMERA_X_POS = 0
CAMERA_Y_POS = 0
CAMERA_ON = True  # for testing purposes

'''