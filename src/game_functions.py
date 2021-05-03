import pygame
import sys
from moviepy.editor import *
    
start_surface_active = True
start_active = False
about_us_active = False
pause_active = False
background_image1 = pygame.image.load('src/images/bcakground_start.jpg')
background_image2 = pygame.image.load('src/images/background_game.png')
background_image3 = pygame.image.load('src/images/background_game_pause.png')
mouse_cursor = pygame.image.load('src/images/光标.png')


def update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message, return_button,
                     continue_button, save_button, save_and_exit_button, exit_button):
    '''更新屏幕上的所有元素'''
    global background_image1
    global background_image2
    global background_image3#其实可以不要，因为写在外面是全局变量了，所以可以直接使用，但是如果是要赋值的话，则必须要global，因为函数不知道是新定义的还是全局变量的
    
    #游戏同时只能是一个状态，通过这种方式来更新屏幕
    if start_surface_active == True:#绘制开始界面
        screen.blit(background_image1, (0, 0))
        start_button.draw_button()
        load_button.draw_button()
        settings_button.draw_button()
        about_us_button.draw_button()
    elif about_us_active == True:#弹出aboutus界面
        screen.blit(background_image1, (0, 0))
        about_us_message.draw_text()
        return_button.draw_button()
    elif start_active == True:#绘制游戏界面
        screen.blit(background_image2, (0, 0))
    elif pause_active == True:#弹出菜单
        screen.blit(background_image3, (0, 0))
        continue_button.draw_button()
        save_button.draw_button()
        save_and_exit_button.draw_button()
        exit_button.draw_button()
    # change_mouse_cursor(screen, mouse_cursor)#效率太低了，放弃
    pygame.display.update()


def check_events(screen, start_button, load_button, settings_button, about_us_button, return_button,
                 continue_button, save_button, save_and_exit_button, exit_button):
    '''监听事件，所有的鼠标点击和键盘操作都会促使for循环运行'''
    global start_surface_active#一个函数中有一次global就可以了
    global about_us_active
    global background_image1
    global start_active
    global pause_active

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:#键盘操作
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_ESCAPE and start_surface_active == False:#一定要加后面这个条件，否则会导致在开始界面按esc，再按start，使得两个标志的布尔值是一样的，同时为True或False，破坏了标志唯一True的性质
                    pause_active = not pause_active
                    start_active = not start_active
            
            elif event.type == pygame.MOUSEMOTION:#鼠标移动操作
                mouse_position = pygame.mouse.get_pos()
                if start_surface_active == True:#在开始界面才检验
                    check_mouse_on_button(mouse_position, start_button)
                    check_mouse_on_button(mouse_position, load_button)
                    check_mouse_on_button(mouse_position, settings_button)
                    check_mouse_on_button(mouse_position, about_us_button)
                elif about_us_active == True:#在关于我们界面才检验
                    check_mouse_on_button(mouse_position, return_button)
                elif pause_active == True:#在pause界面才检验
                    check_mouse_on_button(mouse_position, continue_button)
                    check_mouse_on_button(mouse_position, save_button)
                    check_mouse_on_button(mouse_position, save_and_exit_button)
                    check_mouse_on_button(mouse_position, exit_button)

            elif event.type == pygame.MOUSEBUTTONDOWN:#鼠标点击操作
                mouse_position = pygame.mouse.get_pos()
                if start_surface_active == True:#在开始界面才检验
                    if start_button.button_rect.collidepoint(mouse_position):#开始游戏
                        start_active = True
                        start_surface_active = False
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
                elif pause_active == True:#在pause界面才检验
                    if continue_button.button_rect.collidepoint(mouse_position):
                        pass
                    if save_button.button_rect.collidepoint(mouse_position):
                        pass
                    if save_and_exit_button.button_rect.collidepoint(mouse_position):
                        pass
                    if exit_button.button_rect.collidepoint(mouse_position):
                        pass


def check_mouse_on_button(mouse_position, button):
    '''检验鼠标在按钮上'''
    if button.button_rect.collidepoint(mouse_position):
        button.button_color = (150, 150, 150)#如果在，按钮变成这个颜色，并重绘按钮
        button.draw_button()
    else:
        button.button_color = (20, 20, 20)#如果不在，按钮恢复原来的颜色并重绘按钮
        button.draw_button()


def video_display(filename):
    '''插入播放一段视频'''
    clip = VideoFileClip(filename)#加载视频
    clip.preview()#播放视频


def change_mouse_cursor(screen, mouse_cursor):
    '''更改光标图形'''
    x, y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    screen.blit(mouse_cursor, (x, y))
