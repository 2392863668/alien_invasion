# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2020/10/18 17:45
"""

import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标识调整飞船位置"""
        if self.move_right:
            self.rect.centerx += 1
        elif self.move_left:
            self.rect.centerx -= 1
