import pygame
import map
import player
import npc

'''
# CONSTANTS / VIDEO SETTINGS
'''

fps = 40  # frame rate (basically)
WINDOW_X, WINDOW_Y = 800, 600  # System window resolution
WINDOW_X_area, WINDOW_Y_area = 320, 240  # Game size (gets scaled up to screen resolution)
WINDOW_SIZE = (WINDOW_X, WINDOW_Y)
clock = pygame.time.Clock()  # Clock for animation events etc

'''
# PYGAME INIT
'''

pygame.init()  # starts pygame
window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))  # creates game window
pygame.display.set_caption("rpg")  # Sets the title for the game window
window_area = pygame.Surface((WINDOW_X_area, WINDOW_Y_area))  # Zooms closer to the player
# world is the object that all graphics get blit(rendered) onto
world = pygame.Surface((1600, 1600))

'''
# LOAD GAME OBJECTS
'''

# load map
print("Loading map")
terrain_default = map.tileset("assets/graphics/overworld.png", 32, 32)  # Creates a tileset for map tiles
current_map_name = "dungeon_roofs"  # The name of the json file that the map data is stored in
current_map = map.Map("maps/" + current_map_name + ".json", terrain_default)
current_map.load_collisions()

# player object
spawn_location_x = 64  # Where to spawn the player (to later be set by map data
spawn_location_y = 32
player = player.Player()

# npc objects
print("Loading NPCs")
npc_list = []  # Will later contain all NPC objects / load from map data file
npc1 = npc.NPC("test")

# spawning players and NPCs
player.spawn(world, spawn_location_x, spawn_location_y)  # spawn the player on the map at position x , y
npc1.spawn(world, 64, 64)

'''
# START GAME LOOP
'''

run = True
start_time = None  # this is used to make things happen for x amount of time
while run:
    pygame.time.delay(int(1000 / fps))  # frame refresh rate


# Player movement, see movement.txt in dev manual


# Check events / key events 1 time, not continuously
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attacking = True
                start_time = pygame.time.get_ticks()

# Check key presses continuously
    keys = pygame.key.get_pressed()

# Stops player walking animation if WASD are not pressed
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


# Graphics (see maps.txt in dev manual)

    # load things into the game world
    current_map.load_terrain(world, 32, 32)  # load tiles that are below the player

    # Check if the player is in front of or behind the NPC.
    if player.T_R[1] > npc1.T_R[1]:
        npc1.draw(world, player, start_time)
        player.draw(world, start_time)  # draw the player
    else:
        player.draw(world, start_time)  # draw the player
        npc1.draw(world, player, start_time)

    current_map.load_buildings(world, 32, 32)  # load tiles that are above the player

    # blit/scale everything to the game window
    window_area.blit(world, (-player.x_pos - 16 + (WINDOW_X_area / 2), -player.y_pos - 16 + (WINDOW_Y_area / 2)))
    pygame.transform.scale(window_area, (WINDOW_X, WINDOW_Y), window)
    pygame.display.flip()
