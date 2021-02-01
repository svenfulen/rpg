'''
I have decided not to work on this feature for now.  It is tedious and not currently needed.

'''

'''
class Box:
    def __init__(self, a, b, c, d):
        self.rect = pygame.Rect(a, b, c, d)
        self.left = a
        self.right = a + c
        self.top = b
        self.bottom = b + d
'''

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
                if self.roof_boxes[box_collided].top <= y * 32 <= self.roof_boxes[box_collided].bottom:
                    if self.roof_boxes[box_collided].left <= x * 32 <= self.roof_boxes[box_collided].right:
                        continue
                else:
                    surface_select.blit(self.tileset[tile_to_blit], [(x * tile_width), (y * tile_height)])

            tile += 1