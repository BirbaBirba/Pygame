import pygame
from settings import cell_size
from player import Player
from tiles import Tile

class Scene():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * cell_size
                y = row_index * cell_size

                if cell == 'X':
                    tile = Tile((x, y), cell_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player = Player((x, y), self.display_surface, cell_size)
                    self.player_group.add(player)

    def run(self):
        # Level Tiles
        self.tiles.draw(self.display_surface)

        # Player
        self.player_group.draw(self.display_surface)
        self.player_group.update()
