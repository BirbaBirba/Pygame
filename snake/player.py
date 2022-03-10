import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, cell_size):
        super().__init__()
        self.size = cell_size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Player movement
        self.velocity = pygame.math.Vector2(0, 0)
        self.tick_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.tick_timer, 2000)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity.x = -1
            self.velocity.y = 0
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 1
            self.velocity.y = 0
        elif keys[pygame.K_UP]:
            self.velocity.x = 0
            self.velocity.y = -1
        elif keys[pygame.K_DOWN]:
            self.velocity.x = 0
            self.velocity.y = 1

    def update(self):
        self.get_input()
        event = pygame.event.get()
        # print(self.velocity.x, self.velocity.y)
        if event.type == self.tick_timer:
            self.rect.x += self.velocity.x * self.size
            self.rect.y += self.velocity.y * self.size
