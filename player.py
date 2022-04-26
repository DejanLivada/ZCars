import pygame
from pygame.math import Vector2


class Igrac:
    def __init__(self, health, score, slika, brzina, pravac, pozicija):
        self.health = health
        self.score = score
        self.slika = slika
        self.brzina: Vector2 = brzina
        self.pravac = pravac
        self.pozicija = pozicija


igrac = Igrac(1, 0, pygame.image.load("igrac.png"), Vector2(5, 0), 0, Vector2(255, 360))
igrac.slika = pygame.transform.scale(igrac.slika, (100, 80))

igrac.slika = pygame.transform.rotate(igrac.slika, igrac.pravac)
