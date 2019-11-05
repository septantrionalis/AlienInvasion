import pygame

pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
image = pygame.image.load("java_logo.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        win.fill((0, 255, 0))
        pygame.draw.rect(win, (255, 0, 0), (50, 50, 50, 50))
        win.blit(image, (200, 200))
        pygame.display.flip()

pygame.quit()
