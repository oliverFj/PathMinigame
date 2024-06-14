import pygame

class Donkey:
    def __init__(self, start_pos, center, radius, margin, speed=2):
        self.position = pygame.Vector2(start_pos)
        self.speed = speed
        self.center = pygame.Vector2(center)
        self.radius = radius
        self.margin = margin

    def update(self, target_pos):
        target_vector = pygame.Vector2(target_pos)
        distance = self.position.distance_to(target_vector)
        if distance > 0:
            direction = (target_vector - self.position).normalize()
            new_position = self.position + direction * min(self.speed * distance / 100, distance)
            if self.is_within_band(new_position):
                self.position = new_position

    def is_within_band(self, pos):
        distance_to_center = self.center.distance_to(pos)
        return (self.radius - self.margin) <= distance_to_center <= (self.radius + self.margin)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), 10)
