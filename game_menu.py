import pygame
import sys
from Buttons import ImageButton

pygame.init()

WIDTH, HEIGHT = 600, 550
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тест")
background = pygame.image.load("back_menu600.jpg")
background_s = pygame.image.load("back_settings600.jpg")
clock = pygame.time.Clock()

cur = pygame.image.load("cursor.png")
pygame.mouse.set_visible(False)


def terminate():
    pygame.quit()
    sys.exit()


def draw_cur():
    x, y = pygame.mouse.get_pos()
    screen.blit(cur, (x, y))


def main_menu():
    button_1 = ImageButton(WIDTH // 2 - (252 // 2), 250, 252, 74, "Начать", "Button_1-1.png", "Button_1.png",
                           "click.mp3")
    button_2 = ImageButton(WIDTH // 2 - (252 // 2), 350, 252, 74, "Настройки", "Button_1-1.png", "Button_1.png",
                           "click.mp3")
    button_3 = ImageButton(WIDTH // 2 - (252 // 2), 450, 252, 74, "Выход", "Button_1-1.png", "Button_1.png",
                           "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("GAME", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()

            if event.type == pygame.USEREVENT and event.button == button_1:
                fade()
                new_game()

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
    audio = ImageButton(WIDTH // 2 - (252 // 2), 250, 252, 74, "Аудио", "Button_1-1.png", "Button_1.png", "click.mp3")
    video = ImageButton(WIDTH // 2 - (252 // 2), 350, 252, 74, "Видео", "Button_1-1.png", "Button_1.png",
                        "click.mp3")
    back = ImageButton(WIDTH // 2 - (252 // 2), 450, 252, 74, "Назад", "Button_1-1.png", "Button_1.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_s, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (0, 0, 0))
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
                for btn in [audio, video, back]:
                    btn.set_pos(WIDTH // 2 - (252 // 2))

            for btn in [audio, video, back]:
                btn.handle_event(event)

        for btn in [audio, video, back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        draw_cur()

        pygame.display.flip()


def video_settings():
    global WIDTH, HEIGHT, screen
    video_1 = ImageButton(WIDTH // 2 - (252 // 2), 180, 252, 74, "600x550", "Button_1-1.png", "Button_1.png",
                          "click.mp3")
    video_2 = ImageButton(WIDTH // 2 - (252 // 2), 280, 252, 74, "1024x650", "Button_1-1.png", "Button_1.png",
                          "click.mp3")
    video_3 = ImageButton(WIDTH // 2 - (252 // 2), 380, 252, 74, "1366x768", "Button_1-1.png", "Button_1.png",
                          "click.mp3")
    back = ImageButton(WIDTH // 2 - (252 // 2), 480, 252, 74, "Назад", "Button_1-1.png", "Button_1.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_s, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (0, 0, 0))
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
                change_mode(1366, 768, pygame.FULLSCREEN)
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
    back_button = ImageButton(WIDTH // 2 - (252 // 2), 250, 252, 74, "Назад", "Button_1-1.png", "Button_1.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("New game", True, (0, 0, 0))
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

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
                back_button.set_pos(WIDTH // 2 - (252 // 2))

            back_button.handle_event(event)

        back_button.check_hover(pygame.mouse.get_pos())
        back_button.draw(screen)

        draw_cur()

        pygame.display.flip()


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
    background_s = pygame.image.load(f"back_settings{WIDTH}.jpg")
    background = pygame.image.load(f"back_menu{WIDTH}.jpg")


if __name__ == "__main__":
    main_menu()
