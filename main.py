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

    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (105, 105, 105)
    LIGHT_GRAY = (211, 211, 211)

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
                    game = Game(screen)
                    game.run()
                elif load_game_button.collidepoint(event.pos):
                    load_game(screen)

        screen.fill(WHITE)

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
