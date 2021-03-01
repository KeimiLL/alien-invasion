import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Inicjalizacja Pygame, ustawień i obiektu ekranu.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    #Utworzenie przycisku Gra.
    play_button = Button(ai_settings, screen, "Play")

    #Utworzenie egzemplarza przeznaczonego do przechowywania danych 
    #statystycznych gry oraz utworzenie egzemplarza klasy Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    #Utworzenie grupy przeznaczonej do przechowywania pocisków.
    bullets = Group()
    aliens = Group()

    #Utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Rozpoczęcie pętli głównej
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)
        
run_game()
