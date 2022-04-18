import pygame
from credits_imena import *
credits_font = pygame.font.SysFont('Consolas', 30)

credits_text_developer = credits_font.render(f"Developer : {developer}", True, (255, 255, 255))
credits_text_teacher = credits_font.render(f"Teacher : {teacher}", True, (255, 255, 255))
credits_consultant = credits_font.render(f"Consultant : {consultant}", True, (255, 255, 255))