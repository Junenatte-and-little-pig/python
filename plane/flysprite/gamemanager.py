# -*- encoding: utf-8 -*-
import pygame

from flysprite.enemyplane import EnemyPlane
from flysprite.heroplane import HeroPlane


class GameManager(object):
    def __init__(self):
        self.__background = pygame.image.load("../feiji/background.png")
        self.__background_rect = self.__background.get_rect()
        pygame.Rect.inflate_ip(self.__background_rect,
                               -self.__background_rect.width >> 2,
                               -self.__background_rect.height >> 2)
        self.__screen = pygame.display.set_mode(
            (self.__background_rect.width, self.__background_rect.height), 0,
            32)  # type: pygame.Surface
        self.hero = None
        self.enemies = pygame.sprite.Group()

    def init_game(self):
        hero_image = pygame.image.load("../feiji/hero.gif")
        self.hero = HeroPlane(self.__screen, 2, hero_image)
        for i in range(0, 3):
            self.enemies.add(EnemyPlane(self.__screen, 2, pygame.image.load(
                "../feiji/enemy-1.gif"), pygame.image.load(
                "../feiji/enemy-2.gif"), pygame.image.load(
                "../feiji/enemy-3.gif")))

    def display(self):
        self.__screen.blit(self.__background.convert(), (0, 0))
        self.hero.display()
        for e in self.enemies:
            if e.is_dead():
                e.reset()
            e.display()
