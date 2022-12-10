
from dino_runner.components.powerups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
import random

class Hammer (PowerUp):
    def __init__ (self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.rect.x = random.choice([280, 295, 350])
