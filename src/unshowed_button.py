import pygame
class unshowed_Button:
    def __init__(self, screen, centerx, centery, width, height):
        """初始化button"""
        self.screen = screen  # 方便在后面的方法中用到
        self.width = width
        self.height = height
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)  # 创建按钮矩形
        # 调整位置
        self.button_rect.centerx = centerx
        self.button_rect.centery = centery