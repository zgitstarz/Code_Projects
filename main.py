# game layout
game_pos = {
	1: "",
	2: "",
	3: "",
	4: "",
	5: "",
	6: "",
	7: "",
	8: "",
	9: "",
}

# possiblities that a player could win
possible_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
				[1, 4, 7], [2, 5, 8], [3, 6, 9],
				[1, 5, 9], [3, 5, 7]]


class GAME(object):
	def __init__(self, p1ch, p2ch):
		self.players = [p1ch, p2ch]

	def __str__(self):
		return "This is a tic tac toe game."
	
	def print_game(self):
		print(f"\t\t\t\t\t {game_pos[1]} | {game_pos[2]} | {game_pos[3]}")
		print(f"\t\t\t\t\t----------")
		print(f"\t\t\t\t\t {game_pos[4]} | {game_pos[5]} | {game_pos[6]}")
		print(f"\t\t\t\t\t----------")
		print(f"\t\t\t\t\t {game_pos[7]} | {game_pos[8]} | {game_pos[9]}")

	# return 1 -> player wins
	# return 0 -> game draw
	# return -1 -> game continues
	def check_winner(self, player):
		draw = True

		for values in game_pos.values():
			if not values:
				draw = False
		if draw:
			return 0

		for p in possible_win:
			if game_pos[p[0]] == game_pos[p[1]] == game_pos[p[2]] == player:
				return 1

	# return -1 -> wrong choice of position
	# return 1 -> can be placed
	def check_available(self, position):
		if position > 9 or position < 1:
			print("Wrong Position!")
			return -1
		if game_pos[position]:
			print("Can't place here!")
			return -1
		return 1

	def get_input(self, player_number):
		pos_in = input(f"Enter your desired position (player {player_number}): ")
		return pos_in
		
	def game_loop(self):
		turn = 0
		win = False
		while not win:
			self.print_game()
			player_input = self.get_input(turn + 1)
			result = self.check_available(int(player_input))

			if result == -1:
				print("Try again")
				continue
			else:
				game_pos[int(player_input)] = self.players[turn]

			result = self.check_winner(self.players[turn])

			if result == 1:
				self.print_game()
				print(f"player {turn + 1} wins!")
				win = True
			elif result == 0:
				self.print_game()
				print("Draw!")
				win = True


			if turn % 2 == 0:
				turn = turn + 1
			elif turn % 2 == 1:
				turn = turn - 1
			# now change player


def main():
	g1 = GAME('X','O')
	g1.game_loop()


if __name__ == '__main__':
	main()
