import pygame
import sys
from moviepy.editor import *
    
start_surface_active = True
about_us_active = False
background_image1 = pygame.image.load('src/images/image1.png')


def update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message, return_button):
    '''更新屏幕上的所有元素'''
    global background_image1
    if start_surface_active == True:
        screen.blit(background_image1, (0, 0))
        start_button.draw_button()
        load_button.draw_button()
        settings_button.draw_button()
        about_us_button.draw_button()
    elif about_us_active == True:
        screen.blit(background_image1, (0, 0))
        about_us_message.draw_text()
        return_button.draw_button()
    pygame.display.update()


def check_events(screen, start_button, load_button, settings_button, about_us_button, return_button):
    '''监听事件，所有的鼠标点击和键盘操作都会促使for循环运行'''
    global start_surface_active#一个函数中有一次global就可以了
    global about_us_active
    global background_image1

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#键盘操作
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                if start_surface_active == True:#在开始界面才检验
                    check_mouse_on_button(mouse_position, start_button)
                    check_mouse_on_button(mouse_position, load_button)
                    check_mouse_on_button(mouse_position, settings_button)
                    check_mouse_on_button(mouse_position, about_us_button)
                if about_us_active == True:#在关于我们界面才检验
                    check_mouse_on_button(mouse_position, return_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if start_surface_active == True:#在开始界面才检验
                    if start_button.button_rect.collidepoint(mouse_position):
                        pass#TODO:开始游戏
                    if load_button.button_rect.collidepoint(mouse_position):
                        pass#TODO:加载存档
                    if settings_button.button_rect.collidepoint(mouse_position):
                        pass#TODO:设置：难度，语言
                    if about_us_button.button_rect.collidepoint(mouse_position):
                        start_surface_active = False
                        screen.blit(background_image1, (0, 0))
                        about_us_active = True
                elif about_us_active == True:#在关于我们界面才检验  #注意要用elif，否则点击一次后，会进入aboutus页面，此时该标志为True，就会进行下面的操作。使得return被点击
                    if return_button.button_rect.collidepoint(mouse_position):
                        start_surface_active = True
                        screen.blit(background_image1, (0, 0))
                        about_us_active = False


def check_mouse_on_button(mouse_position, button):
    '''检验鼠标在按钮上'''
    if button.button_rect.collidepoint(mouse_position):
        button.button_color = (150, 150, 150)#如果在，按钮变成这个颜色，并重绘按钮
        button.draw_button()
    else:
        button.button_color = (20, 20, 20)#如果不在，按钮恢复原来的颜色并重绘按钮
        button.draw_button()


#TODO:
def video_display(filename):
    
    clip = VideoFileClip(filename)#加载视频
    clip.preview()#播放视频