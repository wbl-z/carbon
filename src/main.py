import pygame
from settings import Settings
import game_functions as gf
from button import Button
def main():
    pygame.init()#初始化pygame

    settings = Settings()

    screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)#全屏
    pygame.display.set_caption('carbon neutrality')#标题
    icon = pygame.image.load('src/images/icon.jpeg')#要加src目录，可能是root目录的什么原因，不能直接images/
    pygame.display.set_icon(icon)#标题图标

    screen_rect = screen.get_rect()#获取屏幕的rect参数
    start_button = Button(screen, screen_rect.centerx, screen_rect.centery, 100, 50, (20, 20, 20), (200, 200, 200), 'start')

    while True:
        gf.check_events(screen, start_button)
        # mouse_position = pygame.mouse.get_pos()
        # gf.check_mouse_on_button(mouse_position, start_button)
        # gf.video_display('src/images/1.mp4')
        start_button.draw_button()
        pygame.display.update()

#1
main()