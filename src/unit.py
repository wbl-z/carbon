import pygame
from button import Button
from text import Text
class Unit:
    def __init__(self, screen, centerx, centery, width, height, button_color, txt_color, message, font, font_size):
        self.num = 0
        self.add_button = Button(screen, centerx + 80, centery, 50, 50, button_color, txt_color, '', font, font_size)
        self.subtract_button = Button(screen, centerx - 80, centery, 50, 50, button_color, txt_color, '', font, font_size)
        self.text = Text(screen, centerx, centery, txt_color, str(self.num), font, font_size)

    def draw(self):
        self.add_button.draw_button()
        self.subtract_button.draw_button()
        self.text.draw_text()