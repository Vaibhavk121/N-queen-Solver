from flask import Flask, render_template, request
import os
app = Flask(__name__)


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board, row, n):
    if row >= n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0
    return False


def get_solution(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if solve_n_queens(board, 0, n):
        return board
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    solution = None
    if request.method == 'POST':
        n = int(request.form['n-value'])
        print(f"Received input: {n}")  # Debug print
        solution = get_solution(n)
        print(f"Generated solution: {solution}")  # Debug print
    return render_template('index.html', solution=solution)
@app.route('/solve', methods=['POST'])
def solve():
    n = int(request.form['n-value'])
    solution = get_solution(n)
    return render_template('index.html', solution=solution)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)