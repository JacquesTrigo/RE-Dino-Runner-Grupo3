import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Bird
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0:

            if random.randint(0,2) == 0:
                cactus_type = "SMALL"
            elif random.randint(0, 2) == 1:
                cactus_type = "LARGE"
                self.obstacles.append (Cactus(cactus_type))
            elif random.randint(0, 2) == 2:
                self.obstacles.append (Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                self.death_count += 1
                self.show_menu

                if game.on_death():
                    self.obstacles.remove(obstacle)
                else:
                #game.playing = False

                    break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []