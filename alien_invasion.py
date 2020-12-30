# -*- coding: utf-8 -*-
"""
@Author  : Looking
@Email   : 2392863668@qq.com
@Time    : 2020/10/18 17:02
"""

import pygame

from scoreboard import Scoreboard
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from button import Button
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建 Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建用于存储子弹的组
    bullets = Group()

    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
