import pygame
pygame.init()
mainClock = pygame.time.Clock()

#Couleur menu
beige = (255, 224, 163)
white = (255, 255, 255)
grey = (192, 192, 192)
darker = (170, 170, 170)

#Variables
click = False
running = True

#Fenetre du jeu
screen = pygame.display.set_mode((800, 600))
screen.fill(grey)
pygame.display.set_caption("Quixo")
pygame.display.flip()

#Global Font for All
myfont = pygame.font.SysFont('Courier', 60, bold=True)
button_font = pygame.font.SysFont('Courier', 20)


#Fonction écrire texte
def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    textrect = text_object.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_object, textrect)

#Music and Audio
pygame.mixer_music.load('cmi.mp3')
pygame.mixer_music.play(-1)


#Fonction texte button
#def text_objects(text, font):
#    text_Surface = font.render(text, True, white)
#    return text_Surface, text_Surface.get_rect()

#textSurf, textRect = text_objects("Jouer !", button_font)
#        textRect.center = ( (300+(200/2)), (250+(50/2)) )
#        screen.blit(textSurf, textRect)


#Fonction main
def main_menu():
    while True:

        screen.fill(beige)
        draw_text('QUIXO', myfont, white, screen, 305, 100)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 250, 200, 50)
        button_2 = pygame.Rect(300, 350, 200, 50)
        button_3 = pygame.Rect(300, 450, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_1)
            if click:
                game()
        else:
            pygame.draw.rect(screen, darker, button_1)

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_2)
            if click:
                rules()
        else:
            pygame.draw.rect(screen, darker, button_2)

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, grey, button_3)
            if click:
                credits()
        else:
            pygame.draw.rect(screen, darker, button_3)



        click = False
        # if player quits
        for event in pygame.event.get():
            # event = quit
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du jeu")
            # event = echap
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            # event = click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        screen.fill(beige)

        draw_text('Jeu', myfont, white, screen, 340, 75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def rules():
    running = True
    while running:
        screen.fill(beige)

        draw_text('Règles', myfont, white, screen, 290, 75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def credits():
    running = True
    while running:
        screen.fill(beige)

        draw_text('Crédits', myfont, white, screen, 280, 75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()