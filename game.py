import pygame
from Buttons import ImageButton
from Levels import *
from CutScenes import CutScene
from settings import fps


def game(WIDTH, HEIGHT, fullscreen=0):
    pygame.init()

    clock = pygame.time.Clock()

    screen_width = WIDTH
    screen_height = HEIGHT

    screen = pygame.display.set_mode((screen_width, screen_height),
                                     fullscreen if fullscreen else pygame.RESIZABLE)
    pygame.display.set_caption('Little hero')

    current_size = screen.get_size()

    virtual_surface = pygame.Surface((1000, 1000))

    death_count = 0
    f1 = pygame.font.Font(None, 36)

    tile_size = 50
    game_over = 0
    level = 4
    max_levels = 4
    world_data = None
    start = True

    bg_img = pygame.image.load('img/sky.jpg')
    pygame.mixer.music.load("sound/game_sound.mp3")

    def reset_level(level):
        global world_data
        player.__init__(100, 1000 - 130)
        enemy_group.empty()
        lava_group.empty()
        door_group.empty()
        if level == 1:
            world_data = level_1

        elif level == 2:
            world_data = level_2

        elif level == 3:
            world_data = level_3

        elif level == 4:
            world_data = level_4

        elif level == 5:
            world_data = level_5

        elif level > max_levels:
            world_data = level_1

        world = World(world_data)

        return world

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('img/enemy.png')
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0

        def update(self):
            self.rect.x += self.move_direction
            self.move_counter += 1
            if self.move_counter > 50:
                self.move_direction *= -1
                self.move_counter *= -1

    class Lava(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('img/lava.jpg')
            self.image = pygame.transform.scale(img, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Door(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('img/door.png')
            self.image = pygame.transform.scale(img, (tile_size * 2, tile_size * 2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Player:
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'img/r{num}.png')
                img_right = pygame.transform.scale(img_right, (40, 70))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.dead_image = pygame.image.load('img/ghost.png')
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
            self.in_air = True

        def update(self, game_over):
            dx = 0
            dy = 0
            walk_cooldown = 5

            if game_over == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] and self.jumped is False and self.in_air is False:
                    self.vel_y = -15
                    self.jumped = True
                if key[pygame.K_SPACE] is False:
                    self.jumped = False
                if key[pygame.K_a]:
                    dx -= 5
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_d]:
                    dx += 5
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_a] == False and key[pygame.K_d] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                self.vel_y += 1
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y

                self.in_air = True
                for tile in world.tile_list:
                    if tile[1].colliderect(self.rect.x + dx, self.rect.y,
                                           self.width, self.height):
                        dx = 0
                    if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                           self.width, self.height):
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

                if pygame.sprite.spritecollide(self, enemy_group, False):
                    game_over = -1

                elif pygame.sprite.spritecollide(self, lava_group, False):
                    game_over = -1

                elif pygame.sprite.spritecollide(self, door_group, False):
                    game_over = 1

                self.rect.x += dx
                self.rect.y += dy

            elif game_over == -1:
                self.image = self.dead_image
                if self.rect.y > 200:
                    self.rect.y -= 5

            virtual_surface.blit(self.image, self.rect)

            return game_over

    class World:
        def __init__(self, data):
            self.tile_list = []

            dirt_img = pygame.image.load('img/dirt.jpg')
            grass_img = pygame.image.load('img/grass.jpg')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 3:
                        enemy = Enemy(col_count * tile_size, row_count * tile_size - 3)
                        enemy_group.add(enemy)
                    if tile == 4:
                        lava = Lava(col_count * tile_size, row_count * tile_size)
                        lava_group.add(lava)
                    if tile == 5:
                        door = Door(col_count * tile_size - 9, row_count * tile_size - 38)
                        door_group.add(door)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                virtual_surface.blit(tile[0], tile[1])
            text = f1.render(f'{death_count} deaths', True,
                              (255, 255, 255))
            virtual_surface.blit(text, (0, 0))

    if level == 1:
        world_data = level_1

    elif level == 2:
        world_data = level_2

    elif level == 3:
        world_data = level_3

    elif level == 4:
        world_data = level_4

    elif level == 5:
        world_data = level_5

    player = Player(100, 1000 - 130)
    initialCutScene = CutScene(number=0)
    endCutScene = CutScene(number=1)

    enemy_group = pygame.sprite.Group()
    lava_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()

    world = World(world_data)

    restart_button = ImageButton(1000 // 2 - (252 // 2), 250, 252, 74, "Заново", "data/Button_1-1.png",
                                 "data/Button_1.png", "data/click.mp3")
    exit_button = ImageButton(1000 // 2 - (252 // 2), 350, 252, 74, "Выход", "data/Button_1-1.png", "data/Button_1.png",
                              "data/click.mp3")

    for btn in [restart_button, exit_button]:
        btn.set_pos(WIDTH // 2 - (252 // 2))

    event = 0

    pygame.mixer.music.play(-1)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.USEREVENT and event.button == restart_button:
                world_data = []
                world = reset_level(level)
                game_over = 0
                death_count += 1
            elif event.type == pygame.USEREVENT and event.button == exit_button:
                run = False
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
                restart_button.set_pos(current_size[0] // 2 - (252 // 2), current_size[1] // 2)
                exit_button.set_pos(current_size[0] // 2 - (252 // 2), current_size[1] // 2)

        clock.tick(fps)
        if clock.get_fps() == 0.0:
            continue

        if level == 1 and start:
            initialCutScene.play_cut_scene(screen, virtual_surface, clock)
            del initialCutScene
            start = False

        virtual_surface.blit(bg_img, (0, 0))

        world.draw()

        if game_over == 0:
            enemy_group.update()

        enemy_group.draw(virtual_surface)
        lava_group.draw(virtual_surface)
        door_group.draw(virtual_surface)

        game_over = player.update(game_over)

        scaled_surface = pygame.transform.scale(virtual_surface, current_size)
        screen.blit(scaled_surface, (0, 0))

        for enemy in enemy_group:
            if game_over == 0 and player.rect.colliderect(enemy.rect):
                if player.rect.bottom - player.vel_y < enemy.rect.top:
                    enemy_group.remove(enemy)
                else:
                    game_over = -1

        if game_over == -1:
            for btn in [restart_button, exit_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)
                btn.handle_event(event)

        elif game_over == 1:
            level += 1
            if level < max_levels:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                endCutScene.play_cut_scene(screen, virtual_surface, clock)
                run = False

        pygame.display.update()
    pygame.quit()
