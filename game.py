import pygame
import chess
from board import Board

class Game:
    def __init__(self, screen, board=None):
        self.screen = screen
        self.board = Board(screen, board)
        self.running = True
        self.selected_piece = None
        self.selected_square = None
        self.clock = pygame.time.Clock()  # Ajout de l'horloge pour la gestion du framerate
        self.current_player = chess.WHITE  # Définir le joueur actuel
        self.save_and_quit_button = pygame.Rect(800, 700, 200, 60)  # Bouton "Save and Quit" avec une largeur ajustée

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.save_and_quit_button.collidepoint(event.pos):
                        self.save_game()
                        self.running = False
                    else:
                        self.handle_click(event.pos)

            self.screen.fill((0, 0, 0))  # Remplir l'écran de noir
            self.board.draw_board()  # Dessiner le plateau
            self.board.draw_pieces()  # Dessiner les pièces
            self.draw_save_and_quit_button()  # Dessiner le bouton "Save and Quit"
            pygame.display.flip()  # Mettre à jour l'affichage

            self.clock.tick(120)  # Limite à 60 FPS (frames per second)

        pygame.quit()

    def handle_click(self, pos):
        col, row = pos[0] // 100, 7 - (pos[1] // 100)
        square = chess.square(col, row)
        piece = self.board.pieces.get(square)

        if piece and piece.color == self.current_player:  # Vérifier la couleur de la pièce
            self.selected_piece = piece
            self.selected_square = square
            self.board.highlighted_square = None  # Réinitialiser la surbrillance
        elif self.selected_piece:
            move = chess.Move(self.selected_square, square)
            if move in self.board.chess_board.legal_moves:
                captured_piece = self.board.chess_board.piece_at(square)
                if captured_piece:
                    self.board.captured_pieces[captured_piece.color].append(captured_piece)
                self.board.chess_board.push(move)
                self.selected_piece.move(square, self.board.chess_board)
                self.selected_piece = None
                self.selected_square = None
                self.current_player = chess.BLACK if self.current_player == chess.WHITE else chess.WHITE  # Changer de joueur
                self.board.highlighted_square = None  # Réinitialiser la surbrillance
            else:
                self.board.highlighted_square = square  # Mettre en surbrillance la case
                self.selected_piece = None
                self.selected_square = None

    def draw_save_and_quit_button(self):
        # Couleurs
        GRAY = (105, 105, 105)
        WHITE = (255, 255, 255)

        # Police de caractères
        font = pygame.font.Font(None, 36)

        # Dessiner le bouton
        pygame.draw.rect(self.screen, GRAY, self.save_and_quit_button)

        # Ajouter du texte au bouton
        save_and_quit_text = font.render("Save and Quit", True, WHITE)
        self.screen.blit(save_and_quit_text, (self.save_and_quit_button.x + 20, self.save_and_quit_button.y + 15))

    def save_game(self):
        # Sauvegarder la partie actuelle
        save_file = 'save_game.txt'
        with open(save_file, 'w') as file:
            file.write(self.board.chess_board.fen())
        print("Partie sauvegardée.")
