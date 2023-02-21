
the_board = {'top_l': ' ', 'top_m': ' ', 'top_r': ' ',
			'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
			'low_l': ' ', 'low_m': ' ', 'low_r': ' '}


print("""For game use keys:
top_l(r,m) l - left, r - right, m - mid
mid_l(r,m)
low_l(r,m)""")

def printBoard(board):
	print(f"{board['top_l']}|{board['top_m']}|{board['top_r']}\n-+-+-")
	print(f"{board['mid_l']}|{board['mid_m']}|{board['mid_r']}\n-+-+-")
	print(f"{board['low_l']}|{board['low_m']}|{board['low_r']}")


turn = "X"

try:

	for i in range(9):
		printBoard(the_board)
		move = input(f"Turn off {turn}: ")
		if move == 'q':
			print('Clossing..')
			break

		if move in the_board:
			if the_board[move] == ' ':
				the_board[move] = turn
			else:
				print(f' {move}: used '.center(40, '*'))
		else:
			print('\tthis name not used this game..')
			i -= 1

		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
except KeyboardInterrupt as k:
	print("\nClossing...")
