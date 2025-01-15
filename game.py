import pygame
import chess
from board import Board

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(screen)
        self.running = True
        self.selected_piece = None
        self.clock = pygame.time.Clock()  # Ajout de l'horloge pour la gestion du framerate

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.screen.fill((0, 0, 0))  # Remplir l'écran de noir
            self.board.draw_board()  # Dessiner le plateau
            self.board.draw_pieces()  # Dessiner les pièces
            pygame.display.flip()  # Mettre à jour l'affichage

            self.clock.tick(60)  # Limite à 60 FPS (frames per second)

        pygame.quit()

    def handle_click(self, pos):
        col, row = pos[0] // 100, 7 - (pos[1] // 100)
        square = chess.square(col, row)
        piece = self.board.pieces.get(square)

        if piece and piece.color == chess.WHITE:  # Assure-toi de vérifier la couleur de la pièce
            if self.selected_piece:
                self.selected_piece.move(square, self.board.chess_board)
                self.selected_piece = None
            else:
                self.selected_piece = piece
