import chess
from bot_wrapper import Bot
import random


class RandomBot(Bot):
	''' plays random move '''
	def __init__(self, board: chess.Board, color):
		super().__init__(board, color)

	def get_preferred_move(self) -> chess.Move:
		return random.choice(list(self.board.legal_moves))
