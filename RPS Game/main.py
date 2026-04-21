import pygame
import random
import time

pygame.init()

# Screen setup
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper, Scissors")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont(None, 40)
large_font = pygame.font.SysFont(None, 60)

# Load images
stone_img = pygame.image.load("stone.png")
paper_img = pygame.image.load("paper.png")
scissor_img = pygame.image.load("scissor.png")

img_size = (300, 300)
stone_img = pygame.transform.scale(stone_img, img_size)
paper_img = pygame.transform.scale(paper_img, img_size)
scissor_img = pygame.transform.scale(scissor_img, img_size)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(x, y))
    window.blit(img, rect)


def draw_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        hovered = True
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))
        hovered = False

    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
    window.blit(text_surf, text_rect)

    return hovered


def game_loop():
    running = True

    player_choice = None
    computer_choice = None
    result = None

    Abhinav_score = 0
    computer_score = 0

    round_in_progress = False
    click_handled = False

    animation_images = [stone_img, paper_img, scissor_img]
    animation_index = 0
    last_animation_time = time.time()

    while running:
        window.fill(WHITE)
        current_time = time.time()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        # ANIMATION
        if not round_in_progress:
            if current_time - last_animation_time > 1:
                animation_index = (animation_index + 1) % 3
                last_animation_time = current_time

            img = animation_images[animation_index]
            rect = img.get_rect(center=(width // 2, height // 3))
            window.blit(img, rect)

            stone_hover = draw_button("Stone", 50, 450, 200, 80, RED, (255, 120, 120))
            paper_hover = draw_button("Paper", 300, 450, 200, 80, GREEN, (120, 255, 120))
            scissor_hover = draw_button("Scissor", 550, 450, 200, 80, BLUE, (120, 120, 255))

            if mouse_clicked and not click_handled:
                if stone_hover:
                    player_choice = "stone"
                elif paper_hover:
                    player_choice = "paper"
                elif scissor_hover:
                    player_choice = "scissor"
                else:
                    player_choice = None

                if player_choice:
                    computer_choice = random.choice(["stone", "paper", "scissor"])
                    round_in_progress = True
                    click_handled = True

                    if player_choice == computer_choice:
                        result = "It's a Tie!"
                    elif (player_choice == "stone" and computer_choice == "scissor") or \
                         (player_choice == "paper" and computer_choice == "stone") or \
                         (player_choice == "scissor" and computer_choice == "paper"):
                        result = "Abhinav Wins!"
                        Abhinav_score += 10
                    else:
                        result = "Computer Wins!"
                        computer_score += 10

        # SHOW RESULT
        if round_in_progress:
            player_img = stone_img if player_choice == "stone" else paper_img if player_choice == "paper" else scissor_img
            comp_img = stone_img if computer_choice == "stone" else paper_img if computer_choice == "paper" else scissor_img

            window.blit(player_img, player_img.get_rect(center=(200, 250)))
            window.blit(comp_img, comp_img.get_rect(center=(600, 250)))

            draw_text(result, large_font, BLACK, width // 2, 100)

            next_hover = draw_button("Next Round", 300, 500, 200, 70, (200, 200, 200), (150, 150, 150))

            if mouse_clicked and next_hover:
                round_in_progress = False
                player_choice = None
                computer_choice = None
                result = None
                click_handled = False

        # SCORE
        draw_text(f"Abhinav: {Abhinav_score}", font, BLACK, 150, 40)
        draw_text(f"Computer: {computer_score}", font, BLACK, 650, 40)

        pygame.display.update()

    pygame.quit()


game_loop()