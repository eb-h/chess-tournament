import chess
from bot_wrapper import Bot
import random


class AlphabeticBot(Bot):
	def __init__(self, board: chess.Board, color):
		super().__init__(board, color)

	def get_preferred_move(self) -> chess.Move:
		preferred_move = None
		for move in self.board.legal_moves:
			if not preferred_move:
				preferred_move = move
			else:
				preferred_move = min(move, preferred_move, key=self.board.san)
		return preferred_move
