import pygame
import map
import player

# MODES, CONSTANTS
fps = 40  # frame rate
WINDOW_X, WINDOW_Y = 1024, 768
WINDOW_SIZE = (WINDOW_X, WINDOW_Y)
CAMERA_ZOOM = 3
CAMERA_SIZE = ((WINDOW_X * CAMERA_ZOOM), (WINDOW_Y * CAMERA_ZOOM))
CAMERA_X_POS = 0
CAMERA_Y_POS = 0
CAMERA_ON = True  # for testing purposes
FULL_SCREEN_MODE = False


pygame.init()  # starts pygame
world = pygame.display.set_mode(WINDOW_SIZE)  # creates game window


# Returns a window mode, so you can just say world = set_full_screen(true) or (false)
def set_full_screen(boolean):
    if boolean:
        return pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode(WINDOW_SIZE)  # initializes game window, sets size


pygame.display.set_caption("rpg")  # Sets the title for the game window
camera = pygame.Surface(CAMERA_SIZE)
# static graphics data
terrain_default = map.tileset("assets/graphics/overworld.png", 32, 32)

# current map data
current_map_name = "test_collision_3"
current_map = map.Map("maps/" + current_map_name + ".json", terrain_default)
current_map.load_collisions()

# player object
spawn_location_x = 24
spawn_location_y = 24
player = player.Player()

# loading game objects
player.spawn(world, spawn_location_x, spawn_location_y)  # spawn the player on the map at position x , y

run = True
while run:
    pygame.time.delay(int(1000 / fps))  # frame refresh

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # player controls and collision detection
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:  # check for keystrokes
        player.faceDirection = "U"
        if player.y_pos > current_map.map_bounds_upper:  # check bounds
            current_map.detect_collisions(player)
            if player.can_move_up:
                player.move_up()

    if keys[pygame.K_a]:
        player.faceDirection = "L"
        if player.x_pos > current_map.map_bounds_left:
            current_map.detect_collisions(player)
            if player.can_move_left:
                player.move_left()

    if keys[pygame.K_s]:
        player.faceDirection = "D"
        if player.y_pos < current_map.map_bounds_lower:
            current_map.detect_collisions(player)
            if player.can_move_down:
                player.move_down()

    if keys[pygame.K_d]:
        player.faceDirection = "R"
        if player.x_pos < current_map.map_bounds_right:
            current_map.detect_collisions(player)
            if player.can_move_right:
                player.move_right()

    # game loop actions

    current_map.load_terrain(world, 32, 32)  # load tiles that are below the player
    player.draw(world)  # draw the player, needs to be refreshed every frame
    current_map.load_buildings(world, 32, 32)  # load tiles that are above the player
    CAMERA_X_POS = ((-player.x_pos) * CAMERA_ZOOM) + 300
    CAMERA_Y_POS = ((-player.y_pos) * CAMERA_ZOOM) + 250
    pygame.transform.scale(world, CAMERA_SIZE, camera)  # zooms the camera in
    world.fill((0, 0, 0))  # makes the background black
    if CAMERA_ON:
        world.blit(camera, (CAMERA_X_POS, CAMERA_Y_POS))

    pygame.display.flip()
