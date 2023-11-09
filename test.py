import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Object")

# Load the sound effect
shoot_sound = pygame.mixer.Sound("shoot.mp3")  # Replace with the actual sound file

# Load images and set dimensions
object_image = pygame.transform.scale(pygame.image.load("object.png"), (50, 50))
background_image = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
projectile_image = pygame.transform.scale(pygame.image.load("projectile.png"), (20, 20))

# Object and projectile settings
object_x, object_y = (WIDTH - 50) // 2, (HEIGHT - 50) // 2
object_speed = 5
projectiles = []
projectile_speed = 5
projectile_cooldown = 0.5
last_shoot_time = 0

# Set the desired frame rate (30 FPS)
FPS = 30
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_x, new_y = object_x, object_y

    if keys[pygame.K_LEFT]: new_x -= object_speed
    if keys[pygame.K_RIGHT]: new_x += object_speed
    if keys[pygame.K_UP]: new_y -= object_speed
    if keys[pygame.K_DOWN]: new_y += object_speed

    object_x, object_y = [min(max(0, new_x), WIDTH - 50), min(max(0, new_y), HEIGHT - 50)]

    current_time = time.time()
    if keys[pygame.K_SPACE] and (current_time - last_shoot_time) >= projectile_cooldown:
        projectiles.append((object_x + (50 - 20) / 2, object_y))
        last_shoot_time = current_time
        # Play the shooting sound
        shoot_sound.play()

    win.fill((0, 0, 0))
    win.blit(background_image, (0, 0))
    win.blit(object_image, (object_x, object_y))

    new_projectiles = [(px, py - projectile_speed) for px, py in projectiles if py > 0]
    projectiles = new_projectiles

    for px, py in projectiles:
        win.blit(projectile_image, (px, py))

    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()
