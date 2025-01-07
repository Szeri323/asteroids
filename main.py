import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfiled import AsteroidField

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroidfiled = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colision(player):
                print("Game over!")
                return
        screen.fill((1,1,1))
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
        

if __name__ == "__main__":
    main()
