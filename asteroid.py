from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50) #degrees
            orig_vel = self.velocity
            new_vel1 = orig_vel.rotate(angle)
            new_vel2 = orig_vel.rotate(-1*angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position[0], self.position[1], new_rad)
            new_ast2 = Asteroid(self.position[0], self.position[1], new_rad)
            new_ast1.velocity = new_vel1 * 1.2
            new_ast2.velocity = new_vel2 * 1.2

