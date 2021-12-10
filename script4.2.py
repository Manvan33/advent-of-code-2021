#!/usr/bin/python3.9

def parse_input(input: list[str]) -> tuple[list[int], list[list[int]]]:   
    order = [int(number) for number in input.pop(0).split(",")]
    boards = []
    board = []
    board_line = []
    for line in input:
        if line.strip() == "":
            if len(board):
                boards.append(board)
            board = []
            board_line = []
        else:
            board_line = [int(number) for number in line.split()]
            board.append(board_line)
    return order, boards

def blank_markings(board_size, boards_amount) -> list[list[int]]:
    boards = []
    for i in range(boards_amount):
        board = []
        for line in range(board_size):
            board_line = [0 for s in range(board_size)]
            board.append(board_line)
        boards.append(board)
    return boards

def check_win(board: list[list[int]]) -> bool:
    col_sums = [0 for e in board[0]]
    for i, line in enumerate(board):
        if sum(line) == 5:
            return True
        for j in range(len(line)):
            col_sums[j] += line[j]
    if 5 in col_sums:
        return True

def calculate_score(board: list[list[int]], markings: list[list[int]]):
    score = 0
    for line in range(len(board)):
        for col in range(len(board)):
            if markings[line][col] == 0:
                score += board[line][col]
    return score

def main():
    with open("input4") as input_file:
        order, boards = parse_input(input_file.readlines())
        markings = blank_markings(5, len(boards))
    for draw in order:
        # print(draw)
        board = 0
        max = len(boards)
        while board < max:
            for line in range(5):
                for column in range(5):
                    if boards[board][line][column] == draw:
                        # print(board, line, column, draw)
                        markings[board][line][column] = 1
            if check_win(markings[board]):
                winner = {'board': boards[board], 'markings': markings[board], 'draw': draw}
                boards.pop(board)
                markings.pop(board)
                max -= 1
            else :
                board += 1
    print(winner)
    print(calculate_score(winner['board'], winner['markings'])*winner['draw'])

                
if __name__ == "__main__":
    main()