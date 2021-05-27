import pygame
from moviepy.editor import *
import time


start_surface_active = True
start_active = False
about_us_active = False
pause_active = False

trees_surface_active = True
factory_surface_active = False
propaganda_surface_active = False

tree_surface = pygame.image.load('src/images/tree_surface.png')
factory_surface = pygame.image.load('src/images/factory_surface.png')
propaganda_surface = pygame.image.load('src/images/propaganda_surface.png')
background_game_pause = pygame.image.load('src/images/background_game_pause.png')
background_start = pygame.image.load('src/images/background_start.jpg')
# mouse_cursor = pygame.image.load('src/images/光标.png')
# trees_image = pygame.image.load('src/images/land_image.bmp')
# factory_image = pygame.image.load('src/images/land_image.bmp')
# propaganda_image = pygame.image.load('src/images/land_image.bmp')
year = 21
month = 1


def update_screen(screen, start_button, load_button, settings_button, about_us_button, about_us_message, return_button,
				  continue_button, save_button, save_and_exit_button, exit_button, factory_button, money_text,
				   date_text, land_text, c_text, support_text, tree1, tree2, tree3, factory1, factory2, factory3,
				    propaganda1, propaganda2, propaganda3):
	"""更新屏幕上的所有元素"""
	global background_image1
	global background_image2
	global background_image3
	# 其实可以不要，因为写在外面是全局变量了，所以可以直接使用，但是如果是要赋值的话，则必须要global，因为函数不知道是新定义的还是全局变量的
	# 游戏同时只能是一个状态，通过这种方式来更新屏幕
	if start_surface_active:  # 绘制开始界面
		screen.blit(background_start, (0, 0))
		start_button.draw_button()
		load_button.draw_button()
		settings_button.draw_button()
		about_us_button.draw_button()
		exit_button.draw_button()
	elif about_us_active:  # 弹出about us界面
		screen.blit(background_start, (0, 0))
		about_us_message.draw_text()
		return_button.draw_button()
	elif start_active:  # 绘制游戏界面
		if trees_surface_active:#树界面下的界面更新
			screen.blit(tree_surface, (0, 0))
			tree1.draw()
			tree2.draw()
			tree3.draw()
		elif factory_surface_active:#工厂界面下的界面更新
			screen.blit(factory_surface, (0, 0))
			factory1.draw()
			factory2.draw()
			factory3.draw()
		elif propaganda_surface_active:#宣传界面下的界面更新
			screen.blit(propaganda_surface, (0, 0))#TODO：
			propaganda1.draw()
			propaganda2.draw()
			propaganda3.draw()
		#一直保持更新的数据
		money_text.draw_text()
		date_text.draw_text()
		land_text.draw_text()
		c_text.draw_text()
		support_text.draw_text()
	elif pause_active:  # 弹出菜单
		screen.blit(background_game_pause, (0, 0))
		continue_button.draw_button()
		save_button.draw_button()
		save_and_exit_button.draw_button()
		exit_button.draw_button()
	# change_mouse_cursor(screen, mouse_cursor)#效率太低了，放弃
	pygame.display.update()


def check_events(screen, start_button, load_button, settings_button, about_us_button, return_button,
				 continue_button, save_button, save_and_exit_button, exit_button, trees_button,
				  factory_button, propaganda_button, tree1, tree2, tree3, factory1, factory2, factory3,
				   propaganda1, propaganda2, propaganda3):
	"""监听事件，所有的鼠标点击和键盘操作都会促使for循环运行"""
	global start_surface_active  # 一个函数中有一次global就可以了
	global about_us_active
	global background_image1
	global start_active
	global pause_active
	global trees_surface_active
	global factory_surface_active
	global propaganda_surface_active

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:  # 键盘操作
			if event.key == pygame.K_q:
				sys.exit()
			elif (event.key == pygame.K_ESCAPE) and (not start_surface_active):  # 一定要加后面这个条件，否则会导致在开始界面按esc，
												# 再按start，使得两个标志的布尔值是一样的，同时为True或False，破坏了标志唯一True的性质
				pause_active = not pause_active
				start_active = not start_active
				if pygame.mixer.music.get_busy(): # 正在播放则返回True
					pygame.mixer.music.pause()
				else:
					pygame.mixer.music.unpause()

		elif event.type == pygame.MOUSEMOTION:  # 鼠标移动操作
			mouse_position = pygame.mouse.get_pos()
			if start_surface_active:  # 在开始界面才检验
				check_mouse_on_button(mouse_position, start_button)
				check_mouse_on_button(mouse_position, load_button)
				check_mouse_on_button(mouse_position, settings_button)
				check_mouse_on_button(mouse_position, about_us_button)
				check_mouse_on_button(mouse_position, exit_button)
			elif about_us_active:  # 在关于我们界面才检验
				check_mouse_on_button(mouse_position, return_button)
			elif pause_active:  # 在pause界面才检验
				check_mouse_on_button(mouse_position, continue_button)
				check_mouse_on_button(mouse_position, save_button)
				check_mouse_on_button(mouse_position, save_and_exit_button)
				check_mouse_on_button(mouse_position, exit_button)

		elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击操作
			mouse_position = pygame.mouse.get_pos()
			if start_surface_active:  # 在开始界面才检验
				if start_button.button_rect.collidepoint(mouse_position):  # 开始游戏
					start_active = True
					start_surface_active = False
				if load_button.button_rect.collidepoint(mouse_position):
					pass  # TODO:加载存档
				if settings_button.button_rect.collidepoint(mouse_position):
					pass  # TODO:设置：难度，语言
				if about_us_button.button_rect.collidepoint(mouse_position):
					start_surface_active = False
					# screen.blit(background_image1, (0, 0))
					about_us_active = True
				if exit_button.button_rect.collidepoint(mouse_position):
					sys.exit()
			elif about_us_active:  # 在about us界面才检验  #注意要用elif，否则点击一次后，会进入about us页面，此时该标志为True，就会进行下面的操作。使得return被点击
				if return_button.button_rect.collidepoint(mouse_position):
					start_surface_active = True
					# screen.blit(background_image1, (0, 0))
					about_us_active = False
			elif pause_active:  # 在pause界面才检验
				if continue_button.button_rect.collidepoint(mouse_position):
					pause_active = not pause_active
					start_active = not start_active
					if pygame.mixer.music.get_busy(): # 正在播放则返回True
						pygame.mixer.music.pause()
					else:
						pygame.mixer.music.unpause()
				if save_button.button_rect.collidepoint(mouse_position):
					pass # TODO:
				if save_and_exit_button.button_rect.collidepoint(mouse_position):
					pass # TODO:
				if exit_button.button_rect.collidepoint(mouse_position):
					sys.exit()
			elif start_active:	#在游戏界面检验
				if trees_button.button_rect.collidepoint(mouse_position):
					trees_surface_active = True
					factory_surface_active = False
					propaganda_surface_active = False
				if factory_button.button_rect.collidepoint(mouse_position):
					trees_surface_active = False
					factory_surface_active = True
					propaganda_surface_active = False
				if propaganda_button.button_rect.collidepoint(mouse_position):
					trees_surface_active = False
					factory_surface_active = False
					propaganda_surface_active = True
				
				if trees_surface_active:#在树的界面检验加减
					if tree1.add_button.button_rect.collidepoint(mouse_position):
						tree1.num += 1
						tree1.text.message = str(tree1.num)
						tree1.text.prepare_message()
					if tree1.subtract_button.button_rect.collidepoint(mouse_position) and tree1.num > 0:
						tree1.num -= 1
						tree1.text.message = str(tree1.num)
						tree1.text.prepare_message()
					if tree2.add_button.button_rect.collidepoint(mouse_position):
						tree2.num += 1
						tree2.text.message = str(tree2.num)
						tree2.text.prepare_message()
					if tree2.subtract_button.button_rect.collidepoint(mouse_position) and tree2.num > 0:
						tree2.num -= 1
						tree2.text.message = str(tree2.num)
						tree2.text.prepare_message()
					if tree3.add_button.button_rect.collidepoint(mouse_position):
						tree3.num += 1
						tree3.text.message = str(tree3.num)
						tree3.text.prepare_message()
					if tree3.subtract_button.button_rect.collidepoint(mouse_position) and tree3.num > 0:
						tree3.num -= 1
						tree3.text.message = str(tree3.num)
						tree3.text.prepare_message()
				elif factory_surface_active:
					if factory1.add_button.button_rect.collidepoint(mouse_position):
						factory1.num += 1
						factory1.text.message = str(factory1.num)
						factory1.text.prepare_message()
					if factory1.subtract_button.button_rect.collidepoint(mouse_position) and factory1.num > 0:
						factory1.num -= 1
						factory1.text.message = str(factory1.num)
						factory1.text.prepare_message()
					if factory2.add_button.button_rect.collidepoint(mouse_position):
						factory2.num += 1
						factory2.text.message = str(factory2.num)
						factory2.text.prepare_message()
					if factory2.subtract_button.button_rect.collidepoint(mouse_position) and factory2.num > 0:
						factory2.num -= 1
						factory2.text.message = str(factory2.num)
						factory2.text.prepare_message()
					if factory3.add_button.button_rect.collidepoint(mouse_position):
						factory3.num += 1
						factory3.text.message = str(factory3.num)
						factory3.text.prepare_message()
					if factory3.subtract_button.button_rect.collidepoint(mouse_position) and factory3.num > 0:
						factory3.num -= 1
						factory3.text.message = str(factory3.num)
						factory3.text.prepare_message()
				elif propaganda_surface_active:
					if propaganda1.add_button.button_rect.collidepoint(mouse_position):
						propaganda1.num += 1
						propaganda1.text.message = str(propaganda1.num)
						propaganda1.text.prepare_message()
					if propaganda1.subtract_button.button_rect.collidepoint(mouse_position) and propaganda1.num > 0:
						propaganda1.num -= 1
						propaganda1.text.message = str(propaganda1.num)
						propaganda1.text.prepare_message()
					if propaganda2.add_button.button_rect.collidepoint(mouse_position):
						propaganda2.num += 1
						propaganda2.text.message = str(propaganda2.num)
						propaganda2.text.prepare_message()
					if propaganda2.subtract_button.button_rect.collidepoint(mouse_position) and propaganda2.num > 0:
						propaganda2.num -= 1
						propaganda2.text.message = str(propaganda2.num)
						propaganda2.text.prepare_message()
					if propaganda3.add_button.button_rect.collidepoint(mouse_position):
						propaganda3.num += 1
						propaganda3.text.message = str(propaganda3.num)
						propaganda3.text.prepare_message()
					if propaganda3.subtract_button.button_rect.collidepoint(mouse_position) and propaganda3.num > 0:
						propaganda3.num -= 1
						propaganda3.text.message = str(propaganda3.num)
						propaganda3.text.prepare_message()






def check_mouse_on_button(mouse_position, button):
	"""检验鼠标在按钮上"""
	if button.button_rect.collidepoint(mouse_position):
		button.button_color = (150, 150, 150)  # 如果在，按钮变成这个颜色，并重绘按钮
		button.draw_button()
	else:
		button.button_color = (20, 20, 20)  # 如果不在，按钮恢复原来的颜色并重绘按钮
		button.draw_button()


def video_display(fileName):
	"""插入播放一段视频"""
	clip = VideoFileClip(fileName)  # 加载视频
	clip.preview()  # 播放视频


def change_mouse_cursor(screen, mouseCursor):
	"""更改光标图形"""
	x, y = pygame.mouse.get_pos()
	pygame.mouse.set_visible(False)
	screen.blit(mouseCursor, (x, y))


def BGM(musicFile):
	"""播放音乐"""
	pygame.mixer.init()  # 初始化
	pygame.mixer.music.load(musicFile)  # 加载音乐文件
	pygame.mixer.music.play(loops = -1)  # 开始播放音乐流，第一个参数loop，表示重复次数，如（1），则先播放一次，再重复一次，共两次，-1则表示无限重复
								#第二个start参数控制音乐从哪里开始播放，MP3 和 OGG 使用时间表示播放位置（以秒为单位）


def update_data(money_text, date_text, land_text, c_text, support_text):
	global year
	global month
	if start_active:#在游戏状态才更新数据
		month += 1/10
		if month >= 13:
			month = 1
			year += 1
		date_text.message = str(int(year)) + '年' + str(int(month)) + '月'
		date_text.prepare_message()

		

