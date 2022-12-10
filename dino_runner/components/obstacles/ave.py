import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH

class Bird (Obstacle):
    def __init__(self, images):
        self.type = random.choice(0,2)
        super().__init__(images, self.type)
        self.rect.y = random.choice([280, 295, 350])
        self.rect.x = SCREEN_WIDTH + 500
        self.index = 2

    def draw(self, screen):
        if self.step_index >= 9:
            self.index = 0

        if self.step_index > 5:
            screen.blit(self.images[1].self.rect)
        else:
            screen.blit(self.images[0].self.rect)
        self.index +=1