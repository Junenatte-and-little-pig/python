# -*- encoding: utf-8 -*-
import os
import time

import pygame
from pygame.locals import *

from flysprite.gamemanager import GameManager

if __name__ == "__main__":
    # 初始化
    pygame.init()
    # 设置窗口位置
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 70)
    # 设置标题栏
    pygame.display.set_caption("fly game")
    gm = GameManager()
    gm.init_game()
    while True:
        # 绘制背景
        gm.display()
        # 响应事件，不然会假死
        for event in pygame.event.get():
            # 窗口关闭事件
            if event.type == QUIT:
                exit(0)
        # 相应键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            gm.hero.move_left()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            gm.hero.move_right()
        elif key_pressed[K_w] or key_pressed[K_UP]:
            gm.hero.move_up()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            gm.hero.move_down()
        # 子弹击中敌人
        killed_enemies = pygame.sprite.groupcollide(gm.hero.bullets, gm.enemies,
                                                    False, False,
                                                    pygame.sprite.collide_mask)
        for b in killed_enemies.keys():
            gm.hero.bullets.remove(b)
        for enemy in killed_enemies.values():
            for e in enemy:
                e.reset()
        # 被子弹击中
        for e in gm.enemies:
            if pygame.sprite.spritecollide(gm.hero, e.bullets, False,
                                           pygame.sprite.collide_mask):
                print("you are killed!")
                exit(0)
        # 飞机碰撞
        if pygame.sprite.spritecollide(gm.hero, gm.enemies, False,
                                       pygame.sprite.collide_mask):
            print("you are killed!")
            exit(0)
        # 更新界面
        pygame.display.update()
        time.sleep(0.005)
