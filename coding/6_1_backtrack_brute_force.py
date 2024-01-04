def solve_n_queens(n):
    col = set()
    pos_diag = set()  # r + c
    neg_diag = set()  # r - c

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            sol = ["".join(row) for row in board]
            res.append(sol)
        for c in range(n):
            if c in col or r + c in pos_diag or r - c in neg_diag:
                continue
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            # cleanup
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return res


print(solve_n_queens(4))
