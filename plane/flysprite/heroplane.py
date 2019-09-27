# -*- encoding: utf-8 -*
import pygame

from flysprite.bullet import Bullet


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self, screen, speed, image):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen
        self.image = image
        self.__offset = 5
        self.__x = int((screen.get_width() - self.image.get_width()) / 2)
        self.__y = screen.get_height() - self.image.get_height() - self.__offset
        self.__speed = speed
        self.rect = pygame.Rect(self.__x, self.__y, self.image.get_width(),
                                self.image.get_height())
        self.bullets = pygame.sprite.Group()
        self.__shoot_speed = 0

    def display(self):
        self.__screen.blit(self.image.convert(), self.rect)
        dead_bullets = [b for b in self.bullets if b.is_dead()]
        for b in dead_bullets:
            self.bullets.remove(b)
        self.__shoot_speed += 1
        self.__shoot_speed %= 15
        if self.__shoot_speed == 1:
            self.shoot()
        for bullet in self.bullets:
            bullet.display()
            bullet.move()

    def move_left(self):
        if self.rect.left > -50:
            self.rect.move_ip(-self.__speed, 0)
        else:
            self.rect.left = -50

    def move_right(self):
        if self.rect.left < 310:
            self.rect.move_ip(self.__speed, 0)
        else:
            self.rect.left = 310

    def move_up(self):
        if self.rect.top > 0:
            self.rect.move_ip(0, -self.__speed)
        else:
            self.rect.top = 0

    def move_down(self):
        if self.rect.top < 540:
            self.rect.move_ip(0, self.__speed)
        else:
            self.rect.top = 540

    def shoot(self):
        bullet = Bullet(self.__screen, self.rect.left + 39,
                        self.rect.top - 25, "../feiji/bullet-3.gif", "up", 3)
        self.bullets.add(bullet)
