import sys, pygame
from random import randint
## form sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bluebird-midflap.png')
        self.rect = self.image.get_rect(midbottom = (80, 256))
        self.gravity = 0


    def apply_gravity(self):
        self.gravity += 0.23
        self.rect.y += self.gravity
        if self.rect.bottom >= 412:
            self.rect.bottom = 412


    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -3.5

    def update(self):
        self.apply_gravity()
        self.player_movement()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, y_pos, verse):
        super().__init__()
         
        tube_verse = pygame.image.load('pipe-green.png')
        if verse == "up":
            tube_verse = pygame.transform.rotate(tube_verse, 180)
            y_pos -= 460
        
        self.image = tube_verse
        self.rect = self.image.get_rect(midbottom = (300, y_pos))

    def delete_obj(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.rect.x -= 1
        self.delete_obj()

# Game Functions

def collision_detect():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True

# Variables

pygame.init()
size = width, height = (288, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

y_pos = 0
game_active = True
score = 0

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Background
sky_surf = pygame.image.load('background-day.png')
floor_surf = pygame.image.load('base.png')

# Score
#score_surf = test_font.render(f'{score}', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center = (144, 40))

# Game Active False

title = pygame.image.load('message.png')
gameOver = pygame.image.load('gameover.png')

# Timers
obst_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obst_timer, 3000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == obst_timer:
                y_pos = randint(520, 680)
                obstacle_group.add(Obstacle(y_pos, "up"))
                obstacle_group.add(Obstacle(y_pos, "down"))
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    
    if game_active:

        obstacles = obstacle_group.sprites()
        for obstacle in obstacles:
            if obstacle.rect.right == 80:
                score += 0.5
       
        screen.blit(sky_surf, (0, 0))
        screen.blit(floor_surf, (0, 412))

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        score_surf = test_font.render(f'{int(score)}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (144, 40))
        screen.blit(score_surf, score_rect)
        game_active = collision_detect()

    else:
        screen.blit(sky_surf, (0,0))
        screen.blit(floor_surf, (0, 412))
        screen.blit(title, (52, 112))
        screen.blit(gameOver, (48, 450))
        screen.blit(score_surf, score_rect)
        score = 0
        


    pygame.display.update()
    clock.tick(60)







