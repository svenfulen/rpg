import pygame
import map
import player

# MODES, CONSTANTS
fps = 40  # frame rate
WINDOW_X, WINDOW_Y = 800, 600  # Game window size
WINDOW_X_area, WINDOW_Y_area = 320, 240  # zoom window size
WINDOW_SIZE = (WINDOW_X, WINDOW_Y)

pygame.init()  # starts pygame
window = pygame.display.set_mode((WINDOW_X, WINDOW_Y), pygame.FULLSCREEN)  # creates game window
window_area = pygame.Surface((WINDOW_X_area, WINDOW_Y_area))
world = pygame.Surface((1600, 1600))  # 50X50 tiles max , can be changed


pygame.display.set_caption("rpg")  # Sets the title for the game window
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

    if not keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
        player.walking = False

    if keys[pygame.K_w]:  # check for keystrokes
        player.faceDirection = "U"
        if player.y_pos > current_map.map_bounds_upper:  # check bounds
            current_map.detect_collisions(player)
            if player.can_move_up:
                player.walking = True
                player.move_up()

    if keys[pygame.K_a]:
        player.faceDirection = "L"
        if player.x_pos > current_map.map_bounds_left:
            current_map.detect_collisions(player)
            if player.can_move_left:
                player.walking = True
                player.move_left()

    if keys[pygame.K_s]:
        player.faceDirection = "D"
        if player.y_pos < current_map.map_bounds_lower:
            current_map.detect_collisions(player)
            if player.can_move_down:
                player.walking = True
                player.move_down()

    if keys[pygame.K_d]:
        player.faceDirection = "R"
        if player.x_pos < current_map.map_bounds_right:
            current_map.detect_collisions(player)
            if player.can_move_right:
                player.walking = True
                player.move_right()

    # game loop actions

    current_map.load_terrain(world, 32, 32)  # load tiles that are below the player
    player.draw(world)  # draw the player, needs to be refreshed every frame
    current_map.load_buildings(world, 32, 32)  # load tiles that are above the player

    window_area.blit(world, (-player.x_pos - 16 + (WINDOW_X_area / 2), -player.y_pos - 16 + (WINDOW_Y_area / 2)))
    pygame.transform.scale(window_area, (WINDOW_X, WINDOW_Y), window)
    pygame.display.flip()
