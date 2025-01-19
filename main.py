import pygame
from game import Game

def main():
    pygame.init()
    pygame.mixer.quit()  # Désactive l'initialisation audio

    # Ajout d'un affichage pour vérifier que le mode vidéo est bien initialisé
    try:
        screen = pygame.display.set_mode((1000, 800))  # Augmenter la largeur pour inclure les pièces capturées
        pygame.display.set_caption("Chess Game")
    except pygame.error as e:
        return

    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
