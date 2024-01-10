import pygame
import sys
from Buttons import ImageButton
from game import game

pygame.init()

WIDTH, HEIGHT = 600, 550
FPS = 60
FULLSCREEN = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Little hero")
pygame.mixer.music.load("sound/menu_sound.mp3")
background = pygame.image.load("data/back_menu600.jpg")
background_s = pygame.image.load("data/back_settings600.jpg")

clock = pygame.time.Clock()

cur = pygame.image.load("data/cursor.png")
pygame.mouse.set_visible(False)


def terminate():
    pygame.quit()
    sys.exit()


def draw_cur():
    x, y = pygame.mouse.get_pos()
    screen.blit(cur, (x, y))


def main_menu():
    button_1 = ImageButton(WIDTH // 2 - (252 // 2), 250, 252, 74, "Начать", "data/Button_1-1.png", "data/Button_1.png",
                           "data/click.mp3")
    button_2 = ImageButton(WIDTH // 2 - (252 // 2), 350, 252, 74, "Настройки", "data/Button_1-1.png",
                           "data/Button_1.png", "data/click.mp3")
    button_3 = ImageButton(WIDTH // 2 - (252 // 2), 450, 252, 74, "Выход", "data/Button_1-1.png", "data/Button_1.png",
                           "data/click.mp3")

    pygame.mixer.music.play(-1, 7)

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Little Hero", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            if event.type == pygame.USEREVENT and event.button == button_1:
                new_game()
                terminate()

            if event.type == pygame.USEREVENT and event.button == button_2:
                fade()
                settings_menu()
                for btn in [button_1, button_2, button_3]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            if event.type == pygame.USEREVENT and event.button == button_3:
                running = False
                terminate()

            for btn in [button_1, button_2, button_3]:
                btn.handle_event(event)

        for btn in [button_1, button_2, button_3]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        draw_cur()

        pygame.display.flip()


def settings_menu():
    video = ImageButton(WIDTH // 2 - (252 // 2), 250, 252, 74, "Видео", "data/Button_1-1.png", "data/Button_1.png",
                        "data/click.mp3")
    back = ImageButton(WIDTH // 2 - (252 // 2), 350, 252, 74, "Назад", "data/Button_1-1.png", "data/Button_1.png",
                       "data/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_s, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == video:
                fade()
                video_settings()
                for btn in [video, back]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            for btn in [video, back]:
                btn.handle_event(event)

        for btn in [video, back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        draw_cur()

        pygame.display.flip()


def video_settings():
    video_1 = ImageButton(WIDTH // 2 - (252 // 2), 180, 252, 74, "600x550", "data/Button_1-1.png", "data/Button_1.png",
                          "data/click.mp3")
    video_2 = ImageButton(WIDTH // 2 - (252 // 2), 280, 252, 74, "1024x650", "data/Button_1-1.png", "data/Button_1.png",
                          "data/click.mp3")
    video_3 = ImageButton(WIDTH // 2 - (252 // 2), 380, 252, 74, "1366x768", "data/Button_1-1.png", "data/Button_1.png",
                          "data/click.mp3")
    back = ImageButton(WIDTH // 2 - (252 // 2), 480, 252, 74, "Назад", "data/Button_1-1.png", "data/Button_1.png",
                       "data/click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_s, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (0, 0, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 130))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == video_1:
                change_mode(600, 550)
                for btn in [video_1, video_2, video_3, back]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            if event.type == pygame.USEREVENT and event.button == video_2:
                change_mode(1024, 650)
                for btn in [video_1, video_2, video_3, back]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            if event.type == pygame.USEREVENT and event.button == video_3:
                global FULLSCREEN
                FULLSCREEN = pygame.FULLSCREEN
                change_mode(1366, 768, FULLSCREEN)
                for btn in [video_1, video_2, video_3, back]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            for btn in [video_1, video_2, video_3, back]:
                btn.handle_event(event)

        for btn in [video_1, video_2, video_3, back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        draw_cur()

        pygame.display.flip()


def new_game():
    pygame.quit()
    game(WIDTH, HEIGHT, FULLSCREEN)


def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 100:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(FPS)


def change_mode(w, h, fullscreen=0):
    global WIDTH, HEIGHT, screen, background_s, background

    WIDTH, HEIGHT = w, h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), fullscreen)
    background_s = pygame.image.load(f"data/back_settings{WIDTH}.jpg")
    background = pygame.image.load(f"data/back_menu{WIDTH}.jpg")


if __name__ == "__main__":
    main_menu()
