import pygame
import chess
import math
from Engine import *

X = 400
Y = 400
screen = pygame.display.set_mode((X, Y))
pygame.init()

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

b = chess.Board()

pieces = {
 'p': pygame.image.load('b_pawn.png').convert_alpha(),
 'n': pygame.image.load('b_knight.png').convert_alpha(),
 'b': pygame.image.load('b_bishop.png').convert_alpha(),
 'r': pygame.image.load('b_rook.png').convert_alpha(),
 'q': pygame.image.load('b_queen.png').convert_alpha(),
 'k': pygame.image.load('b_king.png').convert_alpha(),
 'P': pygame.image.load('w_pawn.png').convert_alpha(),
 'N': pygame.image.load('w_knight.png').convert_alpha(),
 'B': pygame.image.load('w_bishop.png').convert_alpha(),
 'R': pygame.image.load('w_rook.png').convert_alpha(),
 'Q': pygame.image.load('w_queen.png').convert_alpha(),
 'K': pygame.image.load('w_king.png').convert_alpha(),
}


def update(screen, board):

	for i in range(64):

		piece = board.piece_at(i)
		if piece == None:
			pass
		else:
			screen.blit(pieces[str(piece)], ((i % 8) * 50, 350 - (i // 8) * 50))

	for i in range(7):
		i = i + 1
		pygame.draw.line(screen, WHITE, (0, i * 50), (400, i * 50))
		pygame.draw.line(screen, WHITE, (i * 50, 0), (i * 50, 400))

	pygame.display.flip()


def main(BOARD, engine, engine_color):

	screen.fill(GREY)
	pygame.display.set_caption('Chess')

	index_moves = []

	status = True
	while (status):
		update(screen, BOARD)

		if BOARD.turn == engine_color:
			BOARD.push(engine(BOARD))
			screen.fill(GREY)

		else:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					status = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					screen.fill(GREY)
					pos = pygame.mouse.get_pos()

					#find which square was clicked
					square = (math.floor(pos[0] / 50), math.floor(pos[1] / 50))
					index = (7 - square[1]) * 8 + (square[0])

					# if piece has already been clicked
					if index in index_moves:

						move = moves[index_moves.index(index)]
						#print(BOARD)
						#print(move)
						BOARD.push(move)
						index = None
						index_moves = []

					# show possible moves
					else:

						piece = BOARD.piece_at(index)

						if piece == None:

							pass
						else:

							all_moves = list(BOARD.legal_moves)
							moves = []
							for m in all_moves:
								if m.from_square == index:

									moves.append(m)

									t = m.to_square

									tx = 50 * (t % 8)
									ty = 50 * (7 - t // 8)
									pygame.draw.rect(screen, GREEN, pygame.Rect(tx, ty, 50, 50), 5)

							index_moves = [a.to_square for a in moves]

		if BOARD.outcome() != None:
			print(BOARD.outcome())
			status = False
			print(BOARD)
	pygame.quit()


main(b, min_max2, False)
