from typing import List, Type

import chess
from bot_wrapper import Bot


class Arbiter:
	board = chess.Board()
	moves_played: List[chess.Move] = []

	def __init__(self, p1: Type[Bot], p2: Type[Bot]):
		p1 = p1(self.board, chess.WHITE)
		p2 = p2(self.board, chess.BLACK)
		assert(p1.color != p2.color)

		while not self.board.is_game_over(claim_draw=True):
			if self.board.turn == chess.WHITE:
				move = p1.get_preferred_move()
			else:
				move = p2.get_preferred_move()

			self.moves_played.append(move)
			self.board.push(move)

		print(self.board)
		print(self.convert_moves_played_to_algebraic_notation())
		print(self.board.outcome(claim_draw=True))

	def convert_moves_played_to_algebraic_notation(self) -> str:
		# replay board to get algebraic notation
		algebraic_moves: List[str] = []
		board = chess.Board()
		for move in self.moves_played:
			algebraic_moves.append(board.san(move))
			board.push(move)
		return ' '.join(algebraic_moves)
