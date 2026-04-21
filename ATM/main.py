import pygame
import time

pygame.init()

# Screen
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("ATM Machine")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GREEN = (100, 255, 150)

font = pygame.font.SysFont(None, 50)

balance = 5000
message = "Welcome to ATM"


def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    window.blit(img, (x, y))


def button(text, x, y, w, h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)

    if rect.collidepoint(mouse):
        pygame.draw.rect(window, BLUE, rect)
        if click[0]:
            return True
    else:
        pygame.draw.rect(window, GREEN, rect)

    draw_text(text, x + 20, y + 10)
    return False


def atm():
    global balance, message

    running = True
    while running:
        window.fill(WHITE)

        draw_text("🏧 ATM MACHINE", 250, 50)
        draw_text(message, 200, 120)

        if button("Check Balance", 250, 200, 300, 60):
            message = f"Balance: {balance}"
            time.sleep(0.2)

        if button("Deposit +100", 250, 280, 300, 60):
            balance += 100
            message = "Deposited 100"

        if button("Withdraw -100", 250, 360, 300, 60):
            if balance >= 100:
                balance -= 100
                message = "Withdrawn 100"
            else:
                message = "Insufficient Balance"

        if button("Exit", 250, 440, 300, 60):
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


atm()