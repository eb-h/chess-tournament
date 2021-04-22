import chess
from abc import ABC, abstractmethod


class Bot(ABC):
	board = None
	color = chess.WHITE

	def __init__(self, board: chess.Board, color):
		self.board = board
		self.color = color

	def receive_next_move(self, move: chess.Move):
		self.board.push(move)

	@abstractmethod
	def get_preferred_move(self) -> chess.Move:
		return NotImplemented


if __name__ == '__main__':
	pass
