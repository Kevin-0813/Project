
#Es el encargado del manejo o gestion del input y display en el estado actual del juego.

import pygame as p
from Chess import ChessEngine

width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}

def loadimages():
    pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("imagenes/" + piece + ".png"), (sq_size, sq_size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("gray"))
    gs = ChessEngine.GameState()
    loadimages()
    running = True
    sqselected = ()
    playerclicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // sq_size
                row = location[1] // sq_size
                if sqselected == (row, col):
                    sqselected = ()
                    playerclicks = []
                else:
                    sqselected= (row, col)
                    playerclicks.append(sqselected)
                if len(playerclicks) == 2:
                    move = ChessEngine.Move(playerclicks[0], playerclicks[1], gs.board)
                    print(move.getchessnotation())
                    gs.makemove(move)
                    sqselected = ()
                    playerclicks =[]
        drawgamestate(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawgamestate(screen, gs):
    drawboard(screen)
    drawpieces(screen, gs.board)

def drawboard(screen):
    colors = [p.Color("white"), p.Color("gray"),]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, (c*sq_size, r*sq_size, sq_size, sq_size))
def drawpieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece =board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c*sq_size, r*sq_size, sq_size, sq_size))

main()