def is_safe(state, row, col):
    for i in range(row):
        if state[i] == col or abs(state[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(n):
    solutions = []

    def backtrack(state, row):
        if row == n:
            solutions.append(state.copy())
            return

        for col in range(n):
            if is_safe(state, row, col):
                state[row] = col

                backtrack(state, row + 1)

    initial_state = [-1] * n

    backtrack(initial_state, 0)

    return solutions


n=int(input("nhap n:"))
solutions = solve_n_queens(n)
print(f"Number of solutions for {n} queens: {len(solutions)}")
for solution in solutions:
    print(solution)