import json
import pygame

# get items from items.json file
with open("data/items.json") as f:
    items = json.load(f)


class Weapon:
    def __init__(self, name):
        # item properties
        self.damage = int(items["equipment"][0]["weapons"][0][name][0]["damage"])
        self.description = str(items["equipment"][0]["weapons"][0][name][0]["description"])
        self.attack_type = str(items["equipment"][0]["weapons"][0][name][0]["attack_type"])
        # item textures
        self.face_up_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up"])
        self.face_down_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down"])
        self.face_left_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left"])
        self.face_right_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right"])

        self.walk_up_texture = [pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up_walk"][0]),
                                pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up_walk"][1]),
                                pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up_walk"][2]),
                                pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up_walk"][3])]

        self.walk_down_texture = [pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down_walk"][0]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down_walk"][1]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down_walk"][2]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down_walk"][3])]

        self.walk_left_texture = [pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left_walk"][0]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left_walk"][1]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left_walk"][2]),
                                  pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left_walk"][3])]

        self.walk_right_texture = [pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right_walk"][0]),
                                   pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right_walk"][1]),
                                   pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right_walk"][2]),
                                   pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right_walk"][3])]

        self.up_attack_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["up_attack"])
        self.down_attack_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["down_attack"])
        self.left_attack_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["left_attack"])
        self.right_attack_texture = pygame.image.load(items["equipment"][0]["weapons"][0][name][0]["textures"][0]["right_attack"])
