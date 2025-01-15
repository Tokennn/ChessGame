import pygame
from game import Game

def main():
    pygame.init()
    pygame.mixer.quit()  # Désactive l'initialisation audio
    
    # Ajout d'un affichage pour vérifier que le mode vidéo est bien initialisé
    try:
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess Game")
        print("Fenêtre du jeu initialisée avec succès.")
    except pygame.error as e:
        print(f"Erreur d'initialisation de la fenêtre: {e}")
        return

    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
