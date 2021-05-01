import pygame
import sys
from moviepy.editor import *


def check_events(screen, start_button):
    '''监听事件，所有的鼠标点击和键盘操作都会促使for循环运行'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#键盘操作
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                check_mouse_on_button(mouse_position, start_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('ok')
                check_mousedown_events(screen, start_button)



def check_mousedown_events(screen, start_button):
    print('let\'s start')


def video_display(filename):
    
    clip = VideoFileClip(filename)#加载视频
    clip.preview()#播放视频


def check_mouse_on_button(mouse_position, button):
    if button.button_rect.collidepoint(mouse_position):
        button.button_color = (150, 150, 150)
        button.draw_button()
    else:
        button.button_color = (20, 20, 20)
        button.draw_button()