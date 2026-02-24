from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        self.shot_cooldown -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-1 * dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-1 * dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        #Start with a unit vector pointing straight up from (0, 0) to (0, 1).
        unit_vector = pygame.Vector2(0, 1)
        #Rotate that vector by the player's rotation, so it's pointing in the same direction as the player.
        rotated_vector = unit_vector.rotate(self.rotation)
        #Multiply the vector by PLAYER_SPEED * dt so that the vector is the length the player should move during this frame.
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        #Add the vector to the player's position to move them.
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        
        new_shot = Shot(self.position[0], self.position[1])
        
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        new_shot.velocity = rotated_vector * PLAYER_SHOOT_SPEED
        