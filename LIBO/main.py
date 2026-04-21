import pygame
import time

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Library System")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)

font = pygame.font.SysFont(None, 50)
small_font = pygame.font.SysFont(None, 35)


def draw_text(text, x, y, font, color):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(x, y))
    window.blit(img, rect)


def loading_animation():
    for i in range(0, 101, 10):
        window.fill(WHITE)
        draw_text("Loading Library...", width//2, 250, font, BLACK)
        draw_text(f"{i}%", width//2, 320, font, BLUE)
        pygame.display.update()
        time.sleep(0.2)


def menu():
    running = True

    while running:
        window.fill(WHITE)

        draw_text("📚 Library System", width//2, 100, font, BLACK)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Buttons
        def button(text, x, y):
            rect = pygame.Rect(x, y, 300, 60)

            if rect.collidepoint(mouse):
                pygame.draw.rect(window, BLUE, rect)
                if click[0]:
                    return True
            else:
                pygame.draw.rect(window, (180, 180, 180), rect)

            draw_text(text, x + 150, y + 30, small_font, BLACK)
            return False

        if button("Add Book", 250, 200):
            print("Add Book Clicked")

        if button("Show Book", 250, 280):
            print("Show Book Clicked")

        if button("Issue Book", 250, 360):
            print("Issue Book Clicked")

        if button("Return Book", 250, 440):
            print("Return Book Clicked")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


loading_animation()
menu()