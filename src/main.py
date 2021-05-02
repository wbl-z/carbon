import pygame
from settings import Settings
import game_functions as gf
from button import Button
from text import Text
def main():
    pygame.init()#初始化pygame

    settings = Settings()
    #设置窗口
    screen = pygame.display.set_mode(flags = pygame.FULLSCREEN)#全屏
    pygame.display.set_caption('carbon neutrality')#标题
    icon = pygame.image.load('src/images/icon.jpeg')#要加src目录，可能是root目录的什么原因，不能直接images/
    pygame.display.set_icon(icon)#标题图标
    screen_rect = screen.get_rect()#获取屏幕的rect参数
    #设置按钮
    start_button = Button(screen, screen_rect.centerx, screen_rect.centery - 210, 210, 80, (20, 20, 20), (200, 200, 200), 'start', None, 70)
    load_button = Button(screen, screen_rect.centerx, screen_rect.centery - 70, 210, 80, (20, 20, 20), (200, 200, 200), 'load', None, 70)
    settings_button = Button(screen, screen_rect.centerx, screen_rect.centery + 70, 210, 80, (20, 20, 20), (200, 200, 200), 'settings', None, 70)
    about_us_button = Button(screen, screen_rect.centerx, screen_rect.centery + 210, 210, 80, (20, 20, 20), (200, 200, 200), 'about us', None, 70)
    return_button = Button(screen, screen_rect.centerx, screen_rect.centery + 210, 210, 80, (20, 20, 20), (200, 200, 200), 'return', None, 70)
    #设置文本
    about_us_message = Text(screen, screen_rect.centerx, screen_rect.centery, (255, 248, 220) , '我们是由yqs同志主导的麒深工作室', 'simsunnsimsun', 50)
    #播放片头动画
    # gf.video_display('src/images/2.mp4')
    #无限循环直到玩家选退出
    while True:
        gf.check_events(screen, start_button, load_button, settings_button, about_us_button, return_button)
        gf.update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message, return_button)

main()
