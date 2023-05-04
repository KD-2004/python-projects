import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock-Paper-Scissors")

# Load images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")
computer_choice_imgs = {
    "rock": pygame.image.load("rock.png"),
    "paper": pygame.image.load("paper.png"),
    "scissors": pygame.image.load("scissors.png")
}

# Set up fonts
font = pygame.font.SysFont("Arial", 50)

# Set up game variables
player_choice = None
computer_choice = None
result = None

# Set up animation variables
animating = False
animation_step = 0
animation_direction = 1

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not animating:
            # Get player choice based on where the mouse was clicked
            x, y = pygame.mouse.get_pos()
            if x < 267:
                player_choice = "rock"
            elif x < 534:
                player_choice = "paper"
            else:
                player_choice = "scissors"

            # Determine computer choice
            computer_choice = random.choice(["rock", "paper", "scissors"])

            # Determine result
            if player_choice == computer_choice:
                result = "tie"
            elif player_choice == "rock" and computer_choice == "scissors":
                result = "win"
            elif player_choice == "paper" and computer_choice == "rock":
                result = "win"
            elif player_choice == "scissors" and computer_choice == "paper":
                result = "win"
            else:
                result = "lose"

            # Start animation
            animating = True
            animation_step = 0
            animation_direction = 1

    # Update screen
    screen.fill((255, 255, 255))

    # Draw player and computer choices
    screen.blit(rock_img, (0, 0))
    screen.blit(paper_img, (267, 0))
    screen.blit(scissors_img, (534, 0))
    if player_choice:
        if animating:
            player_choice_img = pygame.transform.rotate(
                computer_choice_imgs[player_choice], animation_step * 36)
        else:
            player_choice_img = computer_choice_imgs[player_choice]
        screen.blit(player_choice_img, (0, 250))
    if computer_choice and not animating:
        screen.blit(computer_choice_imgs[computer_choice], (533, 250))

    # Draw result
    if result:
        text = font.render(result.upper(), True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 500))
        screen.blit(text, text_rect)

    # Animate player choice
    if animating:
        animation_step += animation_direction
        if animation_step == 10:
            animation_direction = -1
        elif animation_step == 0:
            animating = False

    # Update display
    pygame.display.update()

    # Delay to control frame rate
    time.sleep(0.02)

# Quit Pygame
pygame.quit()
