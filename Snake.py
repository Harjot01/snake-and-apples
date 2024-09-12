import pygame
import random
from pygame import color
import os
import sys

pygame.mixer.init()
pygame.init()

# adding logo
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# creating game window
set_width = 900
set_height = 600
gamewindow = pygame.display.set_mode((set_width, set_height))

# Backgound image
bgimg = pygame.image.load("Bg_image.jpg")
bgimg = pygame.transform.scale(bgimg, (set_width, set_height)).convert_alpha()

image = pygame.image.load("bgimg.jpg")
image = pygame.transform.scale(image, (500, 500)).convert_alpha()


# Buttons images
replay_button = pygame.image.load('replay_button.png').convert_alpha()
replay_button = pygame.transform.scale(replay_button, (32, 32))
replay_rect = replay_button.get_rect(midbottom=(425, 280))

main_menu_button = pygame.image.load('main_menu_button.png').convert_alpha()
main_menu_button = pygame.transform.scale(main_menu_button, (36, 36))
main_menu_rect = main_menu_button.get_rect(midbottom=(480, 284))

font = pygame.font.Font('Pixeltype.ttf', 64)
play_button_text = font.render('PLAY', True, 'Black')
play_button_rect = play_button_text.get_rect(topleft=(150, 200))

exit_button_text = font.render('EXIT', True, 'Black')
exit_button_rect = exit_button_text.get_rect(topleft=(150, 300))

credit_button_text = font.render('CREDITS', True, 'Black')
credit_button_rect = credit_button_text.get_rect(topleft=(150, 400))

# colors
Blue = (0, 0, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 190, 0)

# Game title
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


def screen_text1(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


custom_font1 = pygame.font.Font('freesansbold.ttf', 32)


def system_screen_text(text, color, x, y):
    system_screen_text = custom_font1.render(text, True, color)
    gamewindow.blit(system_screen_text, [x, y])


custom_font2 = pygame.font.Font('Gameover.otf', 40)


def screen_text2(text, color, x, y):
    screen_text = custom_font2.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


def welcome():
    pygame.mixer.music.load("new_song.ogg")
    pygame.mixer.music.play()

    exit_game = False
    while not exit_game:
        gamewindow.fill((255, 255, 255))
        gamewindow.blit(image, (400, 0))
        pygame.draw.rect(gamewindow, 'Orange', play_button_rect)
        pygame.draw.rect(gamewindow, 'Orange', play_button_rect, 10)
        gamewindow.blit(play_button_text, play_button_rect)

        pygame.draw.rect(gamewindow, 'Orange', exit_button_rect)
        pygame.draw.rect(gamewindow, 'Orange', exit_button_rect, 10)
        gamewindow.blit(exit_button_text, exit_button_rect)

        pygame.draw.rect(gamewindow, 'Orange', credit_button_rect)
        pygame.draw.rect(gamewindow, 'Orange', credit_button_rect, 10)
        gamewindow.blit(credit_button_text, credit_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.stop()
                    gameloop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if credit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    Credits()  
            

        pygame.display.update()
        clock.tick(60)


main_menu_font = pygame.font.Font('font.otf', 50)
main_menu_text = main_menu_font.render('Main Menu', True, 'White')
main_menu_text_rect = main_menu_text.get_rect(midbottom=(422, 350))
# Game Credits


def Credits():
    while True:
        gamewindow.fill((0, 0, 0))
        credit_font = pygame.font.Font('font.otf', 64)
        credit_text1 = credit_font.render(
            'Programmed By Harjot Singh', True, 'White')
        credit_text2 = credit_font.render('Using Pygame', True, 'White')
        gamewindow.blit(credit_text1, (200, 100))
        gamewindow.blit(credit_text2, (300, 200))

        pygame.draw.rect(gamewindow, 'Orange', main_menu_text_rect)
        pygame.draw.rect(gamewindow, 'Orange', main_menu_text_rect, 10)
        gamewindow.blit(main_menu_text, main_menu_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_text_rect.collidepoint(pygame.mouse.get_pos()):
                    welcome()

        pygame.display.update()
        clock.tick(60)


# creating game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 60
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, int(set_width / 1.5))
    food_y = random.randint(20, int(set_height / 1.5))
    score = 0
    init_velocity = 4
    snake_list = []
    snake_length = 1
    # Check if hiscore exists
    if (not os.path.exists("Hiscore.txt")):
        with open("Hiscore.txt", "w") as f:
            f.write(str(0))
    with open("Hiscore.txt", "r") as f:
        Hiscore = f.read()

    while not exit_game:

        if game_over:
            with open("Hiscore.txt", "w") as f:
                f.write(str(Hiscore))
            gamewindow.fill(Black)
            screen_text2("Game Over!", White, 340, 200)
            gamewindow.blit(replay_button, replay_rect)
            gamewindow.blit(main_menu_button, main_menu_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if replay_rect.collidepoint(pygame.mouse.get_pos()):
                        gameloop()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_rect.collidepoint(pygame.mouse.get_pos()):
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # Food of our snake
            apple = pygame.image.load('apple.png')

            def food(food_x, food_y):
                gamewindow.blit(apple, [food_x, food_y])

            # Condition to eat the food
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                score += 10
                pygame.mixer.music.load("Eating sound.wav")
                pygame.mixer.music.play()

                food_x = random.randint(20, int(set_width / 1.5))
                food_y = random.randint(20, int(set_height / 1.5))

                snake_length += 5
                if score > int(Hiscore):
                    Hiscore = score

            gamewindow.fill(Green)
            gamewindow.blit(bgimg, (0, 0))
            system_screen_text("Score: " + str(score) +
                               "  Hiscore: " + str(Hiscore), (0, 0, 0), 5, 5)
            plot_snake(gamewindow, Black, snake_list, snake_size)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                pygame.mixer.music.load("Gameoversound.ogg")
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 0 or snake_x > set_width or snake_y < 0 or snake_y > set_height:
                pygame.mixer.music.load("Gameoversound.ogg")
                pygame.mixer.music.play()
                game_over = True
            food(food_x, food_y)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()



welcome()
