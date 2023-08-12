import pygame
import math
from random import randint
from button import Button

pygame.init()  # initializing pygame to use the methods inside it

screen = pygame.display.set_mode((600, 600))  # making our window

background_color = (255, 211, 110)  # background color for the window
isGameOn = True  # for check if user playing game or not

pygame.display.set_caption("2D-Game: Menu")  # Setting title of our game

# Start button
start_button_img = pygame.image.load("button.png")  # making our button
start_button_img = pygame.transform.scale(start_button_img, (100, 50))  # Resizing our image

# option Button
option_button_img = pygame.image.load("button.png")
option_button_img = pygame.transform.scale(option_button_img, (120, 50))

# Exit button
exit_button_img = pygame.image.load("button.png")
exit_button_img = pygame.transform.scale(exit_button_img, (100, 50))

# block for the game
# user block
user = pygame.image.load("square.png")
user = pygame.transform.scale(user, (50, 50))
user_x, user_y = 270, 500
user_x_change = 0

# correct block
correct = pygame.image.load("tick.png")
correct = pygame.transform.scale(correct, (50, 50))
# correct_y =

# wrong block
wrong = pygame.image.load("remove.png")
wrong = pygame.transform.scale(wrong, (50, 50))

block_y = 50

# for keeping track of the score
score_value = 0

rgb = (255, 245, 109)

font = pygame.font.Font('freesansbold.ttf', 22)
over_font = pygame.font.Font("freesansbold.ttf", 64)

start_button = Button(start_button_img, 300, 250, font, "Start")
option_button = Button(option_button_img, 300, 310, font, "Options")
exit_button = Button(exit_button_img, 300, 370, font, "Exit")


def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (0, 0, 0))
    screen.blit(score, (x, y))

def user_movement(x, y):
    screen.blit(user, (x, y))


def correct_block_movement(x, y):
    screen.blit(correct, (x, y))


def wrong_block_movement(x, y):
    screen.blit(wrong, (x, y))


def distance(x1, y1, x2, y2):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if 49 < d < 51:
        return True
    else:
        return False


def get_random_x():
    random_x = [randint(10, 260), randint(320, 540)]
    random_index = randint(0, 1)
    random_x_1 = random_x[random_index]
    if random_index == 1:
        random_x_2 = random_x[0]
    else:
        random_x_2 = random_x[1]
    return random_x_1, random_x_2


def reset_blocks(x1, x2, y):
    screen.blit(correct, (x1, y))
    screen.blit(wrong, (x2, y))


def play():
    global isGameOn, user_x, user_x_change, block_y, score_value, rgb
    pygame.display.set_caption("2D-Game: play")

    random_x_1, random_x_2 = get_random_x()

    isGameOn = True
    while isGameOn:
        if rgb[0] == 255:
            screen.fill((255, 245, 109))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameOn = False
                # checking is key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        user_x_change = -0.4
                    elif event.key == pygame.K_RIGHT:
                        user_x_change = 0.4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        user_x_change = 0

            block_y += 0.1

            # checking the collision
            d_with_correct = distance(user_x, user_y, random_x_1, block_y)
            d_with_wrong = distance(user_x, user_y, random_x_2, block_y)
            if d_with_correct or block_y >= 610:
                random_x_1, random_x_2 = get_random_x()
                block_y = -100
                if d_with_correct:
                    score_value += 1
            elif d_with_wrong:
                rgb = (222, 160, 87)


            # for user to not go outside boundary
            if user_x >= 540:
                user_x = 540
            elif user_x <= 10:
                user_x = 10

            user_x += user_x_change
            user_movement(user_x, user_y)
            correct_block_movement(random_x_1, block_y)
            wrong_block_movement(random_x_2, block_y)
            show_score(20, 30)
        elif rgb[0] == 222:
            screen.fill(rgb)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isGameOn = False

            over_text = over_font.render("Game Over", True, (252, 255, 231))
            final_score = font.render(f"Final Score: {score_value}", True, (252, 255, 231))
            screen.blit(over_text, (100, 200))
            screen.blit(final_score, (200, 300))

        pygame.display.update()


def option():
    global isGameOn
    while isGameOn:
        screen.fill((233, 239, 192))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameOn = False

        contact = font.render("Contact us for help at: 32125454323231", True, (78, 148, 79))
        screen.blit(contact, (130, 300))

        pygame.display.update()



while isGameOn:
    screen.fill(background_color)  # making screens background color as given color

    start_button.drawButton(screen)  # passing our screen to draw button
    option_button.drawButton(screen)
    exit_button.drawButton(screen)

    mouse_position = pygame.mouse.get_pos()  # getting positon of the mouse it will return a tuple

    for event in pygame.event.get():  # getting all the event occured
        if event.type == pygame.QUIT:  # check if the event is the click one
            isGameOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.checkPress(mouse_position):
                play()
            if option_button.checkPress(mouse_position):
                option()
            if exit_button.checkPress(mouse_position):
                isGameOn = False

    pygame.display.update()
