def possible_numbers(board, index):
    if board[index] > 0:
        return board[index:index + 1]

    for start in range(0, 81, 9):
        row = board[start:start + 9]
        # print(f"{row}")
    row_start = index // 9 * 9
    row = board[row_start:row_start + 9]
    col_start = index - row_start
    col = [v for v in board[col_start:len(board):9]]
    box_start = row_start // 27 * 27 + col_start // 3 * 3
    box = board[box_start:box_start + 3]
    box.extend(board[box_start + 9:box_start + 12])
    box.extend(board[box_start + 18:box_start + 21])
    already = row
    already.extend(col)
    already.extend(box)
    already_set = set(already)
    # print(f"i:{index}:already_set {already_set}")
    possibles = []
    for a in range(1, 10):
        if a not in already_set:
            possibles.append(a)
    return possibles


def solve(board):
    emptys = [i for i in range(81) if board[i] == 0]

    def attempt_fill(index):
        # determine possible nums,
        possibles = possible_numbers(board, index)
        # if none, this is an empty board index that has no possibles,
        # so we messed up, have to communicate to previous iteration
        # so it can undo what it did to create this invalid state
        if len(possibles) == 0:
            return False
        # there is at least one possible, so attempt the possibles
        # with any True result, go to the next boardindex and attempt fill
        for possible in possibles:
            board[index] = possible
            # print(board)
            # go to the next empty
            emptys = [i for i in range(81) if board[i] == 0]
            if len(emptys) == 0:
                return True
            if attempt_fill(emptys[0]):
                return True
        # print(f"no more possibilities for index{index}")
        # print(f"reset board[{index}] to 0")
        board[index] = 0
        return False

    attempt_fill(emptys[0])
    return board

if __name__ == '__main__':
    board = [0, 0, 0, 0, 8, 0, 0, 7, 9,
             0, 0, 0, 4, 1, 9, 0, 0, 5,
             0, 6, 0, 0, 0, 0, 2, 8, 0,
             7, 0, 0, 0, 2, 0, 0, 0, 6,
             4, 0, 0, 8, 0, 3, 0, 0, 1,
             8, 0, 0, 0, 6, 0, 0, 0, 3,
             0, 9, 8, 0, 0, 0, 0, 6, 0,
             6, 0, 0, 1, 9, 5, 0, 0, 0,
             5, 3, 0, 0, 7, 0, 0, 0, 0]
    print(f"starting with:")
    for i, v in enumerate(board):
        print(f"{v if v > 0 else '_'}  ", end="" if i % 9 != 8 else None)
    solve(board)
    print(f"solved with:")
    for i, v in enumerate(board):
        print(f"{v}  ", end="" if i % 9 != 8 else None)

