from flask import Flask, render_template, jsonify, request
import random

app3 = Flask(__name__)  # First Flask app for the first route

@app3.route('/')
def index():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8]
    ]
    return render_template('index.html', win_combinations=win_combinations)


@app3.route('/bot_move', methods=['POST'])
def bot_move():
    board = request.json['board']
    bot_move = get_best_move(board)
    return jsonify({'bot_move': bot_move})


# Define the rest of your functions for app1 here
def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def check_winner(player, board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8]
    ]
    
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing):
    scores = {"X": -1, "O": 1, "draw": 0}
    if check_winner("X", board):
        return scores["X"]
    elif check_winner("O", board):
        return scores["O"]
    elif "" not in board:
        return scores["draw"]
    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score


if __name__ == '__main__':
    app3.run(port=5002, debug=True)