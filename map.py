import json
import spritesheet
import pygame
from PIL import Image


def tileset(tile_img, tile_width, tile_height):
    tile_graphics = Image.open(tile_img)  # the file to load for the tileset
    img_width = int(tile_graphics.width)  # the width of the image in pixels
    img_height = int(tile_graphics.height)  # the height of the image in pixels
    tiles_wide = int(img_width / tile_width)  # the width of the image (# of tiles wide)
    tiles_tall = int(img_height / tile_height)  # the height of the image (# of tiles tall)
    ss = spritesheet.spritesheet(tile_img)  # turns tile image into a sprite sheet object
    tile_return = [0]

    for y in range(0, tiles_tall):  # scan up and down y amount of times
        for x in range(0, tiles_wide):  # scan left to right x amount of times
            tile_return.append(ss.image_at(((x * tile_width), (y * tile_width), tile_width, tile_height)))

    return tile_return


class Box:
    def __init__(self, a, b, c, d):
        self.rect = pygame.Rect(a, b, c, d)
        self.left = a
        self.right = a + c


class Map:
    def __init__(self, filepath, tile_set):
        with open(filepath) as f:
            self.load_map = json.load(f)  # load_map is a dictionary of the json data from the map file
        self.map_width = int(self.load_map["layers"][0]["width"])  # size of the map (# of tiles wide)
        self.map_height = int(self.load_map["layers"][0]["height"])  # size of the map (# of tiles tall)
        self.tileset = tile_set  # array of tile textures
        self.spawn_point = [64, 64]  # spawn point for player (x and y)

        # map bounds, just the edges of the map, try to design maps so the player never hits the edge anyway
        self.map_bounds_left = -8
        self.map_bounds_upper = 0
        self.map_bounds_right = (self.map_width * 32) - 24
        self.map_bounds_lower = (self.map_height * 32) - 32

        # map data
        self.map_tiles = self.load_map["layers"][0]["data"]  # array of which tile textures to be used, bottom layer
        self.map_tiles_2 = self.load_map["layers"][2]["data"]  # array of which tile textures to be used, top layer

        # map collisions
        self.map_collisions = self.load_map["layers"][1]["objects"]  # a dictionary of hit box data
        self.collision_boxes = []  # each location where collisions can occur

        # map roofs load
        self.arr_roofs = self.load_map["layers"][3]["data"]  # roofs raw data (gets drawn)
        self.arr_roofs_rects = self.load_map["layers"][4]["objects"]  # roof collision rects
        self.roof_boxes = []

    def load_terrain(self, surface_select, tile_width, tile_height):  # draws map
        tile = 0
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_to_blit = int(self.map_tiles[tile])
                if tile_to_blit != 0:
                    surface_select.blit(self.tileset[tile_to_blit], [(x * tile_width), (y * tile_height)])
                tile += 1

    def load_roofs(self):
        for box in range(0, len(self.arr_roofs_rects)):
            x_box = int(self.arr_roofs_rects[box]["x"])
            y_box = int(self.arr_roofs_rects[box]["y"])
            width_box = int(self.arr_roofs_rects[box]["width"])
            height_box = int(self.arr_roofs_rects[box]["height"])
            self.roof_boxes.append(Box(x_box, y_box, width_box, height_box))

    def draw_roofs(self, surface_select, player_obj, tile_width, tile_height):  # draws roofs player isn't colliding
        rect_list = [b.rect for b in self.roof_boxes]
        box_collided = player_obj.rect.collidelist(rect_list)

        tile = 0
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_to_blit = int(self.arr_roofs[tile])
                if tile_to_blit != 0:
                    if box_collided == -1:  # if there is no collision with the
                        surface_select.blit(self.tileset[tile_to_blit], [(x * tile_width), (y * tile_height)])
                    elif box_collided != -1:
                        if self.roof_boxes[box_collided].left <= x * 32 <= self.roof_boxes[box_collided].right:
                            continue
                        else:
                            surface_select.blit(self.tileset[tile_to_blit], [(x * tile_width), (y * tile_height)])
                tile += 1

    def load_buildings(self, surface_select, tile_width, tile_height):
        tile = 0
        for y in range(0, self.map_height):
            for x in range(0, self.map_width):
                tile_to_blit = int(self.map_tiles_2[tile])
                if tile_to_blit != 0:
                    surface_select.blit(self.tileset[tile_to_blit], [(x * tile_width), (y * tile_height)])
                tile += 1

    def load_collisions(self):  # loads rect hit boxes for map objects
        for box in range(0, len(self.map_collisions)):
            x_box = int(self.map_collisions[box]["x"])
            y_box = int(self.map_collisions[box]["y"])
            width_box = int(self.map_collisions[box]["width"])
            height_box = int(self.map_collisions[box]["height"])
            self.collision_boxes.append(Box(x_box, y_box, width_box, height_box))

    def detect_collisions(self, player_obj):
        rect_list = [b.rect for b in self.collision_boxes]

        player_obj.can_move_up = player_obj.top_rect.collidelist(rect_list) == -1
        player_obj.can_move_down = player_obj.bottom_rect.collidelist(rect_list) == -1
        player_obj.can_move_left = player_obj.left_rect.collidelist(rect_list) == -1
        player_obj.can_move_right = player_obj.right_rect.collidelist(rect_list) == -1
