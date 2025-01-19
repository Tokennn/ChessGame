import pygame
from game import Game
import chess
import os

def main():
    pygame.init()
    pygame.mixer.quit()  # Désactive l'initialisation audio

    # Ajout d'un affichage pour vérifier que le mode vidéo est bien initialisé
    try:
        screen = pygame.display.set_mode((1100, 800))  # Augmenter la largeur pour inclure les pièces capturées
        pygame.display.set_caption("Chess Game")
    except pygame.error as e:
        return

    background_image = pygame.image.load('images/paysage.jpeg')  # Remplacez par le chemin de votre image
    background_image = pygame.transform.scale(background_image, (1100, 800))  # Redimensionner l'image


    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (105, 105, 105)
    LIGHT_GRAY = (211, 211, 211)
    BACKGROUND_COLOR = (30, 30, 50)  
    HIGHLIGHT_COLOR = (10, 10, 10)


    # Police de caractères
    font = pygame.font.Font(None, 36)

    # Boutons
    new_game_button = pygame.Rect(400, 300, 200, 50)
    load_game_button = pygame.Rect(400, 400, 200, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(event.pos):
                    pygame.draw.rect(screen, HIGHLIGHT_COLOR, new_game_button)
                    pygame.display.flip()
                    pygame.time.delay(100) 
                    game = Game(screen)
                    game.run()
                elif load_game_button.collidepoint(event.pos):
                    pygame.draw.rect(screen, HIGHLIGHT_COLOR, load_game_button)
                    pygame.display.flip()
                    pygame.time.delay(200)
                    load_game(screen)
        screen.fill(BACKGROUND_COLOR)

        screen.blit(background_image, (0, 0))



        # Dessiner les boutons
        pygame.draw.rect(screen, GRAY, new_game_button)
        pygame.draw.rect(screen, GRAY, load_game_button)

        # Ajouter du texte aux boutons
        new_game_text = font.render("New Game", True, WHITE)
        load_game_text = font.render("Load Game", True, WHITE)
        screen.blit(new_game_text, (new_game_button.x + 50, new_game_button.y + 10))
        screen.blit(load_game_text, (load_game_button.x + 50, load_game_button.y + 10))

        pygame.display.flip()

    pygame.quit()

def load_game(screen):
    # Charger la partie sauvegardée
    save_file = 'save_game.txt'
    if os.path.exists(save_file):
        with open(save_file, 'r') as file:
            fen = file.read().strip()
        board = chess.Board(fen)
        game = Game(screen, board)
        game.run()
    else:
        print("Aucune sauvegarde trouvée.")

if __name__ == "__main__":
    main()
