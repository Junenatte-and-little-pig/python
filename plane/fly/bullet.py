# -*- encoding: utf-8 -*-
import pygame


class Bullet(object):
    def __init__(self, screen, x, y, path, direction="up"):
        self.__screen = screen
        self.__path = path
        self.image = pygame.image.load(self.__path)
        self.rect = pygame.Rect(x, y, self.image.get_width(),
                                self.image.get_height())
        self.__direction = direction
        self.__speed = 2

    def display(self):
        self.__screen.blit(self.image.convert(), self.rect)

    def move(self):
        if "up" == self.__direction:
            self.rect.move_ip(0, -self.__speed)
        elif "down" == self.__direction:
            self.rect.move_ip(0, self.__speed)

    def is_dead(self):
        if "up" == self.__direction:
            if self.rect.top < -22:
                return True
            else:
                return False
        elif "down" == self.__direction:
            if self.rect.top > 635:
                return True
            else:
                return False
