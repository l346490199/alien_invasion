#!/bin/python3
#-*- coding: utf-8 -*-
# alien.py
# @author 刘秋
# @email lq@aqiu.info
# @description alien类  外星人
# @created 2019-08-19T11:25:00.241Z+08:00
# @last-modified 2019-08-19T11:35:58.426Z+08:00
#

import pygame
from pygame.sprite import Sprite

class Alien (Sprite):
    ''' 表示单个外星人的类'''

    def __init__(self, ai_settings, screen):
        ''' 初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图形，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精准位置
        self.x = float(self.rect.x)


    def blitme(self):
        ''' 在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)
        