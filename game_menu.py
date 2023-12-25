import pygame
import sys
from Buttons import ImageButton

pygame.init()

WIDTH, HEIGHT = 600, 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тест")
background = pygame.image.load("back.jpg")


def main_menu():
    button_1 = ImageButton(10, 250, 252, 74, "Начать", "Button_1-1.png", "Button_1.png", "click.mp3")
    button_2 = ImageButton(10, 350, 252, 74, "Настройки", "Button_1-1.png", "Button_1.png",
                           "click.mp3")
    button_3 = ImageButton(10, 450, 252, 74, "Выход", "Button_1-1.png", "Button_1.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, -50))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("GAME", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(130, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == button_1:
                new_game()

            if event.type == pygame.USEREVENT and event.button == button_2:
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == button_3:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [button_1, button_2, button_3]:
                btn.handle_event(event)

        for btn in [button_1, button_2, button_3]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()


def settings_menu():
    audio = ImageButton(10, 250, 252, 74, "Аудио", "Button_1-1.png", "Button_1.png", "click.mp3")
    video = ImageButton(10, 350, 252, 74, "Видео", "Button_1-1.png", "Button_1.png",
                           "click.mp3")
    back = ImageButton(10, 450, 252, 74, "Назад", "Button_1-1.png", "Button_1.png", "click.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, -50))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("SETTINGS", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(130, 200))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == back:
                running = False

            for btn in [audio, video, back]:
                btn.handle_event(event)

        for btn in [audio, video, back]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()


def new_game():
    pass


if __name__ == "__main__":
    main_menu()
