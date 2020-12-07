from .piece import Piece


class CrownedPiece(Piece):
    self.king = True

    def make_king(self):
        print("This piece is already crowned.")

    def traverseInOppositeDirection(self):
        if piece.color == RED:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
