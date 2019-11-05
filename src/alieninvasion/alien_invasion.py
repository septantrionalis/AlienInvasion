import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from GameStats import GameStats
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.mixer.init()
    pygame.mixer.music.load("mdust.mp3")
    pygame.mixer.music.play()

    shoot = pygame.mixer.Sound("shoot.wav")
    shoot.set_volume(0.5)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, shoot)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

