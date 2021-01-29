class Camera:
    def __init__(self, window_x, window_y):
        self.top_pos = 0
        self.bottom_pos = 0
        self.left_pos = 0
        self.right_pos = 0

'''
CAMERA_X_POS = ((-player.x_pos) * CAMERA_ZOOM) + 300
    CAMERA_Y_POS = ((-player.y_pos) * CAMERA_ZOOM) + 250
    pygame.transform.scale(world, CAMERA_SIZE, camera)  # zooms the camera in
    camera = pygame.Surface(CAMERA_SIZE)
    CAMERA_ZOOM = 3
CAMERA_SIZE = ((WINDOW_X * CAMERA_ZOOM), (WINDOW_Y * CAMERA_ZOOM))
CAMERA_X_POS = 0
CAMERA_Y_POS = 0
CAMERA_ON = True  # for testing purposes

'''