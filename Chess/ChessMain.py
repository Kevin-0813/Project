
#Es el encargado del manejo o gestion del input y display en el estado actual del juego.

import pygame as p
from Chess import ChessEngine

width = height = 512
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}

def loadImages():
    pieces = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("imagenes/" + piece + ".png"), (sq_size, sq_size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("gray"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGamestate(screen, gs)
        clock.tick(max_fps)
        p.display.flip()

def drawGamestate(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("black"),]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, (c*sq_size, r*sq_size, sq_size, sq_size))
def drawPieces(screen, board):
    pass
main()