
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
    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.MoveLog.append(move)
        self.whiteToMove = not self.whiteToMove

class Move():

    rankstorows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)
    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]