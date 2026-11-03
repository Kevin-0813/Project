
#Guarda toda la informacion del juego actual. Tambien determina los movimientos del juego actual

class GameState():
    def __init__(self):
        #El tablero es 8x8 en una lista 2d, donde cada elemento de la lista tiene 2 caracteres.
        #El primer caracter representa el color de la pieza "b" o "w".
        #El segundo representa que tipo de pieza es "R", "N", "B", "K", "Q" o "P".
        #El "--" representa espacios vacios sin piezas.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["--", "--", "--", "--", "--", "--", "--", "--",],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.MoveLog = []
