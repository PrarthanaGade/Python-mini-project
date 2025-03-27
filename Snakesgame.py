import pygame
import time
import random
from pygame.locals import *

pygame.init()

# Colors for the Snake Game
Background = (0, 0, 0)       # Black
Snake = (15, 52, 96)         # Blue
Food = (233, 69, 96)         # Vibrant Red
Borders = (22, 33, 62)       # Midnight Blue
Score = (0, 255, 255)        # Cyan


win_width = 600
win_height = 400
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

snake = 10
snake_speed = 5

font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("monospace", 30)


def user_score(score):
    number = score_font.render("Score " + str(score), True, Score)
    window.blit(number, [0, 0])

def message(msg):
    msg_surface = font_style.render(msg, True, Score)
    msg_rect = msg_surface.get_rect(center=(win_width / 2, win_height / 2))  # Center the message
    window.blit(msg_surface, msg_rect)

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            window.fill(Background)
            message("You have lost! Press P to play again or Q to quit the game")
            user_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                if event.key == K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                if event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake
                if event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(Background)
        pygame.draw.rect(window, Food, [foodx, foody, snake, snake])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(window, Snake, [segment[0], segment[1], snake, snake])

        user_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
