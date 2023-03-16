import pygame

pygame.init()

keep_going = True
screen = pygame.display.set_mode([800, 500])

win = pygame.Surface([500, 250])
win_rect = win.get_rect(center=screen.get_rect().center)

f = pygame.font.Font('resources/3dumb.ttf', 70)
text = f.render("Game over", True, (246, 198, 1), (0, 100, 120))
text_2 = f.render(f"Scores: {5}", True, (246, 198, 1))
text_rect = text.get_rect(centerx=win_rect.centerx)
text_2_rect = text_2.get_rect()


while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    screen.fill((127, 127, 127))
    win.fill((137, 137, 137))
    win.blit(text, text_rect)
    # win.blit(text_2, text_2_rect)
    screen.blit(win, win_rect)
    pygame.display.update()

pygame.quit()
