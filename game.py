import pygame
from player import Player
import math

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Circle parameters
WIDTH, HEIGHT = 800, 600
circle_center = (WIDTH // 2, HEIGHT // 2)
circle_radius = 200
margin = 20  # Variable length from the line
finish_line_length = 40  # Length of the finish lines
finish_line_gap = 20  # Distance between the two finish lines

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hold markøren inden for banen")
        self.font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()
        self.players = [Player("Player1", RED, (circle_center[0], circle_center[1] - circle_radius), circle_center, circle_radius, margin)]
        self.game_active = False
        self.donkey_crossed_first_line = False

    def start(self):
        self.game_active = True
        self.donkey_crossed_first_line = False
        for player in self.players:
            player.reset_position()
            player.reset_score()

    def update(self):
        if self.game_active:
            for player in self.players:
                player.update()
                mouse_pos = pygame.mouse.get_pos()
                if not player.is_within_band(mouse_pos, circle_center, circle_radius, margin):
                    player.reset_position()
                    player.reset_score()

                if self.check_first_finish_line_cross(player.donkey):
                    self.donkey_crossed_first_line = True

                if self.check_second_finish_line_cross(player.donkey):
                    if self.donkey_crossed_first_line:
                        player.increment_score()
                        print(f"{player.name} crossed both finish lines!")
                        self.donkey_crossed_first_line = False

    def draw(self):
        self.screen.fill(WHITE)
        if self.game_active:
            self.draw_circle()
            self.draw_finish_lines()
            for player in self.players:
                player.draw(self.screen)
                self.draw_text(f"{player.name} Score: {player.get_score()}", (10, 10), player.color)
        else:
            self.draw_text("Tryk ENTER for at starte", (250, 250), BLACK)
            self.draw_text("Tryk ESC for at afslutte", (250, 300), BLACK)

    def draw_circle(self):
        pygame.draw.circle(self.screen, GREEN, circle_center, circle_radius + margin, 5)
        pygame.draw.circle(self.screen, GREEN, circle_center, circle_radius - margin, 5)

    def draw_finish_lines(self):
        # First finish line at approximately 11:55
        angle1 = math.radians(-5)
        x1_outer = circle_center[0] + (circle_radius + margin) * math.cos(angle1)
        y1_outer = circle_center[1] + (circle_radius + margin) * math.sin(angle1)
        x1_inner = circle_center[0] + (circle_radius - margin) * math.cos(angle1)
        y1_inner = circle_center[1] + (circle_radius - margin) * math.sin(angle1)
        pygame.draw.line(self.screen, BLUE, (x1_outer, y1_outer), (x1_inner, y1_inner), 5)

        # Second finish line at approximately 01:05
        angle2 = math.radians(5)
        x2_outer = circle_center[0] + (circle_radius + margin) * math.cos(angle2)
        y2_outer = circle_center[1] + (circle_radius + margin) * math.sin(angle2)
        x2_inner = circle_center[0] + (circle_radius - margin) * math.cos(angle2)
        y2_inner = circle_center[1] + (circle_radius - margin) * math.sin(angle2)
        pygame.draw.line(self.screen, BLUE, (x2_outer, y2_outer), (x2_inner, y2_inner), 5)

    def check_first_finish_line_cross(self, donkey):
        # Check if the donkey has crossed the first finish line (at approximately 11:55)
        angle1 = math.radians(-5)
        x1_inner = circle_center[0] + (circle_radius - margin) * math.cos(angle1)
        y1_inner = circle_center[1] + (circle_radius - margin) * math.sin(angle1)
        x1_outer = circle_center[0] + (circle_radius + margin) * math.cos(angle1)
        y1_outer = circle_center[1] + (circle_radius + margin) * math.sin(angle1)
        return (min(x1_inner, x1_outer) <= donkey.position.x <= max(x1_inner, x1_outer)) and (min(y1_inner, y1_outer) <= donkey.position.y <= max(y1_inner, y1_outer))

    def check_second_finish_line_cross(self, donkey):
        # Check if the donkey has crossed the second finish line (at approximately 01:05)
        angle2 = math.radians(5)
        x2_inner = circle_center[0] + (circle_radius - margin) * math.cos(angle2)
        y2_inner = circle_center[1] + (circle_radius - margin) * math.sin(angle2)
        x2_outer = circle_center[0] + (circle_radius + margin) * math.cos(angle2)
        y2_outer = circle_center[1] + (circle_radius + margin) * math.sin(angle2)
        return (min(x2_inner, x2_outer) <= donkey.position.x <= max(x2_inner, x2_outer)) and (min(y2_inner, y2_outer) <= donkey.position.y <= max(y2_inner, y2_outer))

    def draw_text(self, text, pos, color):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, pos)

# Run the game
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game.start()
                elif event.key == pygame.K_ESCAPE:
                    running = False

        game.update()
        game.draw()
        pygame.display.flip()
        game.clock.tick(60)

    pygame.quit()
