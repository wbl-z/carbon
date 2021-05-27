import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from button import Button
from text import Text
from land import Land
from unshowed_button import unshowed_Button
from unit import Unit
import threading, time

def main():
    pygame.init() # 初始化pygame
    settings = Settings() # 设置窗口
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN) # 全屏
    pygame.display.set_caption('carbon neutrality')# 标题
    icon = pygame.image.load('src/images/icon.jpeg')# 要加src目录，可能是root目录的什么原因，不能直接images/
    pygame.display.set_icon(icon)# 标题图标
    screen_rect = screen.get_rect()# 获取屏幕的rect参数
    # 设置开始菜单按钮
    start_button = Button(screen, screen_rect.centerx, screen_rect.centery - 190, 210, 80, (20, 20, 20), (200, 200, 200), 'start', None, 70)
    load_button = Button(screen, screen_rect.centerx, screen_rect.centery - 90, 210, 80, (20, 20, 20), (200, 200, 200), 'load', None, 70)
    settings_button = Button(screen, screen_rect.centerx, screen_rect.centery + 10, 210, 80, (20, 20, 20), (200, 200, 200), 'settings', None, 70)
    about_us_button = Button(screen, screen_rect.centerx, screen_rect.centery + 110, 210, 80, (20, 20, 20), (200, 200, 200), 'about us', None, 70)
    return_button = Button(screen, screen_rect.centerx, screen_rect.centery + 110, 210, 80, (20, 20, 20), (200, 200, 200), 'return', None, 70)
    # 设置弹出菜单按钮
    continue_button = Button(screen, screen_rect.centerx, screen_rect.centery - 210, 210, 80, (20, 20, 20), (200, 200, 200), 'continue', None, 70)
    save_button = Button(screen, screen_rect.centerx, screen_rect.centery - 70, 210, 80, (20, 20, 20), (200, 200, 200), 'save', None, 70)
    save_and_exit_button = Button(screen, screen_rect.centerx, screen_rect.centery + 70, 210, 80, (20, 20, 20), (200, 200, 200), 'save&exit', None, 70)
    exit_button = Button(screen, screen_rect.centerx, screen_rect.centery + 210, 210, 80, (20, 20, 20), (200, 200, 200), 'exit', None, 70)
    # 设置文本
    about_us_message = Text(screen, screen_rect.centerx, screen_rect.centery, (255, 248, 220), '我们是由zzb同志主导的{[()]}工作室', 'simsunnsimsun', 50)
    # 创建土地精灵组，玩家选项精灵组
    # #放弃这种方法，不实现种树
    # lands = Group()
    # for line in range(4):
    #     for rank in range(4):
    #         land = Land(screen, 600 + rank * 50, 300 + line * 50, 50, 50)
    #         lands.add(land)
    #可支配部件框
    #1.底部3个选项
    trees_button = unshowed_Button(screen, screen_rect.centerx + 460, screen_rect.centery + 320, 150, 150)#TODO:大小位置待调整
    propaganda_button = unshowed_Button(screen, screen_rect.centerx + 20, screen_rect.centery + 320, 150, 150)
    factory_button = unshowed_Button(screen, screen_rect.centerx - 425, screen_rect.centery + 320, 150, 150)
    #2.四个角的各种数据
    money_text = Text(screen, screen_rect.width - 100, screen_rect.height - 40, (0, 0, 0), '资金', 'simsunnsimsun', 30)
    date_text = Text(screen, 100, 40, (0, 0, 0), '时间', 'simsunnsimsun', 30)
    land_text = Text(screen, 100, screen_rect.height - 40, (0, 0, 0), '土地剩余', 'simsunnsimsun', 30)
    c_text = Text(screen, screen_rect.centerx, 40, (0, 0, 0), '碳排放', 'simsunnsimsun', 30)
    support_text = Text(screen, screen_rect.width - 100, 40, (0, 0, 0), '支持率', 'simsunnsimsun', 30)
    #3.1树的三个组件
    tree1 = Unit(screen, screen_rect.centerx - 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    tree2 = Unit(screen, screen_rect.centerx, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    tree3 = Unit(screen, screen_rect.centerx + 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    #3.2工厂的三个组件
    factory1 = Unit(screen, screen_rect.centerx - 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    factory2 = Unit(screen, screen_rect.centerx, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    factory3 = Unit(screen, screen_rect.centerx + 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    #3.3宣传的三个组件
    propaganda1 = Unit(screen, screen_rect.centerx - 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    propaganda2 = Unit(screen, screen_rect.centerx, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    propaganda3 = Unit(screen, screen_rect.centerx + 400, screen_rect.centery + 150, 210, 80, (20, 20, 20), (200, 200, 200), '数目', 'simsunnsimsun', 30)
    # 播放片头动画
    # gf.video_display('src/images/开头动画0.mp4')
    # 播放音乐
    # gf.BGM('src/images/music.mp3')
    # 无限循环直到玩家选退出
    
    #多线程失败，原因未知
    # t = threading.Thread(target = gf.dayin())
    
    # t.setDaemon(True)
    # t.start()
    last_time = 0
    while True:
        
        if (time.time() - last_time) > 1:
            last_time = time.time()
            gf.update_data(money_text, date_text, land_text, c_text, support_text)
        gf.check_events(screen, start_button, load_button, settings_button, about_us_button, return_button, continue_button, save_button, save_and_exit_button, exit_button, trees_button, factory_button, propaganda_button, tree1, tree2, tree3, factory1, factory2, factory3, propaganda1, propaganda2, propaganda3)
        gf.update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message, return_button, continue_button, save_button, save_and_exit_button, exit_button, factory_button, money_text, date_text, land_text, c_text, support_text, tree1, tree2, tree3, factory1, factory2, factory3, propaganda1, propaganda2, propaganda3)

main()

