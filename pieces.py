import chess

class Piece:
    def __init__(self, color, position, piece_type):
        self.color = color
        self.position = position
        self.piece_type = piece_type

    def get_legal_moves(self, board):
        raise NotImplementedError("Subclasses should implement this method")

    def move(self, to_position, board):
        board.push(chess.Move(self.position, to_position))
        self.position = to_position

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.KING)

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.QUEEN)

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.BISHOP)

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.KNIGHT)

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.ROOK)

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, chess.PAWN)
