import pygame
from pygame.sprite import Sprite
class Land(Sprite):
    def __init__(self, screen, centerx, centery, width, height):
        super().__init__()
        self.screen = screen
        # self.image = pygame.image.load('src/images/land_image.bmp') # 必须要这样命名，因为调用Group中的draw时，其实就是重复调用
        #                                                         # surface.blits((spr.image, spr.rect) for spr in sprites)
        # self.rect = self.image.get_rect() # 同上
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.centerx = centerx
        self.rect.centery = centery

