# -*- encoding: utf-8 -*
import random

import pygame

from fly.bullet import Bullet


class EnemyPlane(object):
    def __init__(self, screen):
        self.__screen = screen
        self.image = pygame.image.load("../feiji/enemy-1.gif")
        self.__offset = 5
        self.__x = random.randint(0,
                                  self.__screen.get_width() - self.image.get_width())
        self.__y = random.choice([-40, -90, -120])
        self.__speed = 1
        self.rect = pygame.Rect(self.__x, self.__y, self.image.get_width(),
                                self.image.get_height())
        self.bullets = []
        self.__directions = ["left", "right"]
        self.__direction = self.__directions[random.randint(0, 1)]

    def reset(self):
        self.rect = pygame.Rect(random.randint(0, 360 - 55),
                                random.choice([-40, -90, -120]), 51, 39)

    def display(self):
        self.__screen.blit(self.image.convert(), self.rect)
        self.move()
        if 66 == random.randint(1, 200):
            self.shoot()
        for bullet in self.bullets:
            bullet.display()
            bullet.move()

    def move(self):
        self.rect.move_ip(0, self.__speed)
        if "left" == self.__direction:
            self.rect.move_ip(-self.__speed, 0)
        elif "right" == self.__direction:
            self.rect.move_ip(self.__speed, 0)
        if self.rect.left >= 315:
            self.__direction = "left"
        elif self.rect.left <= 0:
            self.__direction = "right"

    def shoot(self):
        bullet = Bullet(self.__screen,
                        self.rect.left + self.image.get_width() >> 1,
                        self.rect.top + self.image.get_height() >> 1,
                        "../feiji/bullet-1.gif", "down")
        self.bullets.append(bullet)

    def is_dead(self):
        if self.rect.top > 700:
            return True
        else:
            return False
