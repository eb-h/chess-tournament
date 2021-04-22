from arbiter import Arbiter
from random_bot import RandomBot
import chess

if __name__ == '__main__':
	b = chess.Board()
	Arbiter(RandomBot, RandomBot)
