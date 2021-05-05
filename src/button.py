import pygame


class Button:
    def __init__(self, screen, centerX, centerY, width, height, button_color, txt_color, message, font, font_size):
        """初始化button"""
        self.message_image_rect = self.message_image.get_rect()  # 获取参数
        self.message_image = self.font.render(self.message, True,
                                              self.txt_color)  #
        self.screen = screen  # 方便在后面的方法中用到
        self.width = width
        self.height = height
        self.button_color = button_color
        self.txt_color = txt_color
        self.message = message
        self.active = False  # 用于实现鼠标悬停按钮的变化
        self.font = pygame.font.SysFont(font, font_size)  # 第一个是字体类型，会在系统中查找，第二个字体大小，第三个参数是是否为bold，第四个是是否为italic

        self.button_rect = pygame.Rect(0, 0, self.width, self.height)  # 创建按钮矩形
        # 调整位置
        self.button_rect.centerx = centerX
        self.button_rect.centery = centerY

        self.prepare_message()  # 放在__init__中，从而一开始就有

    def prepare_message(self):
        """把msg渲染成图像，并使其在按钮上居中"""
        # 把字体文件渲染成图像，第一个参数是文本信息，第二个是是否开启防锯齿，即是否让边缘平滑，第三个是字体颜色，第四个是背景的颜色，这个背景是刚好把文字包括起来的一个矩形，不填则为透明背景
        self.message_image_rect.center = self.button_rect.center

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        self.screen.blit(self.message_image, self.message_image_rect)
