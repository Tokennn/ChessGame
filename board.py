import pygame
import chess
import os
from pieces import King, Queen, Bishop, Knight, Rook, Pawn

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.chess_board = chess.Board()
        self.pieces = self.create_pieces()
        self.piece_images = self.load_piece_images()
        self.captured_pieces = {chess.WHITE: [], chess.BLACK: []}  # Liste pour stocker les pièces capturées
        self.highlighted_square = None  # Case en surbrillance

    def create_pieces(self):
        pieces = {}
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                piece = self.chess_board.piece_at(square)
                if piece:
                    piece_class = self.get_piece_class(piece)
                    pieces[square] = piece_class(piece.color, square)
        return pieces

    def get_piece_class(self, piece):
        if piece.piece_type == chess.PAWN:
            return Pawn
        elif piece.piece_type == chess.KNIGHT:
            return Knight
        elif piece.piece_type == chess.BISHOP:
            return Bishop
        elif piece.piece_type == chess.ROOK:
            return Rook
        elif piece.piece_type == chess.QUEEN:
            return Queen
        elif piece.piece_type == chess.KING:
            return King

    def load_piece_images(self):
        piece_images = {}
        color_names = {chess.WHITE: "white", chess.BLACK: "black"}
        piece_types = {
            chess.PAWN: "PAWN",
            chess.KNIGHT: "KNIGHT",
            chess.BISHOP: "BISHOP",
            chess.ROOK: "ROOK",
            chess.QUEEN: "QUEEN",
            chess.KING: "KING"
        }

        current_dir = os.path.dirname(__file__)
        images_loaded = True  # Variable pour vérifier si toutes les images sont chargées

        for color in [chess.WHITE, chess.BLACK]:
            for piece_type in piece_types:
                image_path = os.path.join(current_dir, 'images', f"{color_names[color]}_{piece_types[piece_type]}.png")
                if os.path.exists(image_path):
                    piece_images[(color, piece_type)] = pygame.image.load(image_path).convert_alpha()
                else:
                    images_loaded = False  # Si une image est manquante

        if not images_loaded:
            print("Certaines images sont manquantes. Assurez-vous que toutes les images sont présentes dans le dossier 'images'.")
        return piece_images

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = (105, 105, 105) if (row + col) % 2 == 0 else (211, 211, 211)
                pygame.draw.rect(self.screen, color, pygame.Rect(col * 100, row * 100, 100, 100))

    def draw_pieces(self):
        self.pieces = self.create_pieces()  # Mettre à jour les pièces après chaque mouvement
        for square, piece in self.pieces.items():
            col, row = chess.square_file(square), 7 - chess.square_rank(square)
            piece_image = self.piece_images.get((piece.color, piece.piece_type))
            if piece_image:
                self.screen.blit(piece_image, pygame.Rect(col * 100, row * 100, 100, 100))

        self.draw_captured_pieces()  # Dessiner les pièces capturées
        self.draw_highlighted_square()  # Dessiner la case en surbrillance

    def draw_captured_pieces(self):
        # Dessiner les pièces capturées à côté de l'échiquier
        for color in [chess.WHITE, chess.BLACK]:
            x_offset = 850 if color == chess.WHITE else 950
            y_offset = 50
            for piece in self.captured_pieces[color]:
                piece_image = self.piece_images.get((piece.color, piece.piece_type))
                if piece_image:
                    self.screen.blit(piece_image, pygame.Rect(x_offset, y_offset, 100, 100))
                    y_offset += 100

    def draw_highlighted_square(self):
        if self.highlighted_square is not None:
            col, row = chess.square_file(self.highlighted_square), 7 - chess.square_rank(self.highlighted_square)
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(col * 100, row * 100, 100, 100), 5)  # Dessiner un rectangle rouge
