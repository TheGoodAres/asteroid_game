from circleshape import *
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position ,self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < -150:
            self.position.x = SCREEN_WIDTH
        elif self.position.x >SCREEN_WIDTH + 150:
            self.position.x = 0
        elif self.position.y < -150:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT + 150:
            self.position.y = 0

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            degree = random.uniform(20,50)
            vector1 = self.velocity.rotate(degree)
            vector2 = self.velocity.rotate(-degree)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            Asteroid(self.position[0], self.position[1], new_radius).velocity = vector1 * 1.2
            Asteroid(self.position[0], self.position[1], new_radius).velocity = vector2 * 1.2
