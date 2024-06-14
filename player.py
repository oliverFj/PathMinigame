import pygame
from score import Score
from donkey import Donkey

class Player:
    def __init__(self, name, color, start_pos, center, radius, margin):
        self.name = name
        self.color = color
        self.start_pos = start_pos
        self.score = Score()
        self.donkey = Donkey(start_pos, center, radius, margin)
        self.reset_position()

    def reset_position(self):
        pygame.mouse.set_pos(self.start_pos)

    def increment_score(self):
        self.score.increment()

    def reset_score(self):
        self.score.reset()

    def get_score(self):
        return self.score.get_score()
    
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, self.color, mouse_pos, 5)
        self.donkey.draw(screen, self.color)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.donkey.update(mouse_pos)
    
    def is_within_band(self, pos, center, radius, margin):
        dx = pos[0] - center[0]
        dy = pos[1] - center[1]
        distance_squared = dx * dx + dy * dy
        outer_radius_squared = (radius + margin) ** 2
        inner_radius_squared = (radius - margin) ** 2
        return inner_radius_squared <= distance_squared <= outer_radius_squared
