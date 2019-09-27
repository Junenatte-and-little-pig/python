# -*- encoding: utf-8 -*-
import os

import pygame
from pygame.locals import *

if __name__ == "__main__":
    # 初始化
    pygame.init()
    # 设置窗口位置
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 70)
    # 设置标题栏
    pygame.display.set_caption("fly game")
    screen = pygame.display.set_mode((360, 613), 0, 32)  # type: pygame.Surface
    # screen: pygame.Surface = pygame.display.set_mode((360, 613), 0, 32) 定义时制定类型，但并不约束
    # 加载背景图片
    background = pygame.image.load("../feiji/background.png").convert()
    # 加载飞机
    hero = pygame.image.load("../feiji/hero.gif").convert()
    # 飞机左上顶点位置
    x, y = 130, 480
    # 飞机移动速度
    speed = 1
    while True:
        # 绘制背景
        screen.blit(background, (0, 0))
        # 绘制飞机
        screen.blit(hero, (x, y))
        # 响应事件，不然会假死
        for event in pygame.event.get():
            # 窗口关闭事件
            if event.type == QUIT:
                exit(0)
        # 相应键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("left")
            if x > 0:
                x -= speed
            else:
                x = 0
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("right")
            if x < 260:
                x += speed
            else:
                x = 260
        elif key_pressed[K_w] or key_pressed[K_UP]:
            print("up")
            if y > 0:
                y -= speed
            else:
                y = 0
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            print("down")
            if y < 480:
                y += speed
            else:
                y = 480
        # 更新界面
        pygame.display.update()
