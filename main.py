import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = 0

    pygame.display.set_caption('Show Text')
    
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    end_game = False
     
    Player.containers= (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while not end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
                break
        
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if player.check_for_collision(object):
                print("Game over!")
                end_game = True
                break
            for shot in shots:
                if object.check_for_collision(shot):
                    shot.kill()
                    object.split()
                    score += 1

        screen.fill("black")

        update_text_on_screen(score, screen)
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    print(f"Your score: {score}")


def update_text_on_screen(score, screen):
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"score: {score}", True, white)
    textRect = text.get_rect()
    screen.blit(text, textRect)
if __name__ == "__main__":
    main()