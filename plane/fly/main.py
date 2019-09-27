# -*- encoding: utf-8 -*-
import os
import time

import pygame
from pygame.locals import *

from fly.enemyplane import EnemyPlane
from fly.heroplane import HeroPlane

if __name__ == "__main__":
    # 初始化
    pygame.init()
    # 设置窗口位置
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 70)
    # 设置标题栏
    pygame.display.set_caption("fly game")
    # 加载背景图片
    # background = pygame.image.load("../feiji/background.png").convert()
    background = pygame.image.load("../feiji/background.png")
    background_rect = background.get_rect()
    pygame.Rect.inflate_ip(background_rect, -background_rect.width >> 2,
                           -background_rect.height >> 2)
    screen = pygame.display.set_mode(
        (background_rect.width, background_rect.height), 0,
        32)  # type: pygame.Surface
    hero = HeroPlane(screen)
    enemies = [EnemyPlane(screen) for x in range(0, 3)]
    while True:
        # 绘制背景
        screen.blit(background.convert(), (0, 0))
        hero.display()
        for e in enemies:
            if e.is_dead():
                e.reset()
            e.display()
        # 响应事件，不然会假死
        for event in pygame.event.get():
            # 窗口关闭事件
            if event.type == QUIT:
                exit(0)
        # 相应键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            hero.move_left()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            hero.move_right()
        elif key_pressed[K_w] or key_pressed[K_UP]:
            hero.move_up()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            hero.move_down()
        elif key_pressed[K_SPACE]:
            # 发射子弹
            hero.shoot()
        # 飞机碰撞
        if -1 != hero.rect.collidelist(enemies):
            print("you are killed!")
            exit(0)
        # 更新界面
        pygame.display.update()
        time.sleep(0.005)
