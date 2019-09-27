# -*- encoding: utf-8 -*
import random

import pygame

from flysprite.bullet import Bullet


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self, screen, speed, *images):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.__images = images
        self.image = random.choice(self.__images)
        self.__offset = 5
        self.__x = random.randint(0,
                                  self.__screen.get_width() - self.image.get_width())
        self.__y = random.choice(
            [-self.image.get_height(), -self.image.get_height() * 2,
             -self.image.get_height() * 3])
        self.__speed = 1
        self.rect = pygame.Rect(self.__x, self.__y, self.image.get_width(),
                                self.image.get_height())
        self.bullets = pygame.sprite.Group()
        self.__directions = ["left", "right"]
        self.__direction = self.__directions[random.randint(0, 1)]

    def reset(self):
        self.image = random.choice(self.__images)
        self.__x = random.randint(0,
                                  self.__screen.get_width() - self.image.get_width())
        self.__y = random.choice([-40, -90, -120])
        self.rect = pygame.Rect(self.__x, self.__y, self.image.get_width(),
                                self.image.get_height())
        self.__direction = self.__directions[random.randint(0, 1)]

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
                        "../feiji/bullet-1.gif", "down", 2)
        self.bullets.add(bullet)

    def is_dead(self):
        if self.rect.top > 700:
            return True
        else:
            return False
