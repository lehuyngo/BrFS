


n = int()
board = list()

def is_safe(row, column):
    for i in range(column):
        if row == board[i] or abs(row - board[i]) == column - i:
            return False
    return True

def depth_first_search(n):
    # solutions = list()
    solutions_count = 0
    stack = list()
    for irow in range(n):
        stack.append((irow,0))
    while len(stack) != 0:
            # print(stack)
            # print(board)
            #print("stack",stack)
            (row, column) = stack.pop(0)
            board[column] = row
            next_column = column + 1
            if next_column > n-1:
                # solutions.append(deepcopy(board))
                solutions_count += 1
                # for column, row in enumerate(board):
                #     print(row, column)
                # print()
                print(board)
                continue
            stack_this_state=list()
            for i in range(n):
                if is_safe(i, next_column):
                    stack_this_state.append((i, next_column))
            stack=stack_this_state+stack
    # return solutions
    return solutions_count

if __name__ == '__main__':
    n = int(input('N: '))
    board = [-1] * n
    solutions_count = depth_first_search(n)
    print(solutions_count)
    # solutions = depth_first_search(n)
    # print(solutions)
