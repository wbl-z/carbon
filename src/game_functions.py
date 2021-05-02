import pygame
import sys
from moviepy.editor import *
    
start_surface_active = True
    
about_us_active = False


def update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message):
    '''更新屏幕上的所有元素'''
    if start_surface_active == True:
        start_button.draw_button()
        load_button.draw_button()
        settings_button.draw_button()
        about_us_button.draw_button()
    elif about_us_active == True:
        screen.fill((0, 0, 0))
        about_us_message.draw_text()
    pygame.display.update()


def check_events(screen, start_button, load_button, settings_button, about_us_button):
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
                check_mouse_on_button(mouse_position, load_button)
                check_mouse_on_button(mouse_position, settings_button)
                check_mouse_on_button(mouse_position, about_us_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if start_button.button_rect.collidepoint(mouse_position):
                    pass#TODO:开始游戏
                if load_button.button_rect.collidepoint(mouse_position):
                    pass#TODO:加载存档
                if settings_button.button_rect.collidepoint(mouse_position):
                    pass#TODO:设置：难度，语言
                if about_us_button.button_rect.collidepoint(mouse_position):
                    global start_surface_active
                    start_surface_active = False
                    screen.fill((0, 0, 0))
                    global about_us_active
                    about_us_active = True


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
    import cv2

    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    # clip = VideoFileClip(filename)#加载视频
    # clip.preview()#播放视频
