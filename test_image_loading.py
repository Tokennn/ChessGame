import pygame

# Initialiser Pygame
pygame.init()

# Créer une fenêtre pour l'affichage
screen = pygame.display.set_mode((800, 800))  # Taille arbitraire de la fenêtre

# Charger une image pour tester
image_path = '/home/chouaib/ChestGame/images/white_PAWN.png'
try:
    image = pygame.image.load(image_path).convert_alpha()
    print("Image chargée avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement de l'image : {e}")

# Attendre que l'utilisateur ferme la fenêtre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
