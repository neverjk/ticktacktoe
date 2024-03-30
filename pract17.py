def display_board(board):
    print("  |  |")
    print("" + board[1] + " | " + board[2] + "| " + board[3])
    print("  |  |")
    print("---------")
    print("  |  |")
    print("" + board[4] + " | " + board[5] + "| " + board[6])
    print("  |  |")
    print("---------")
    print("  |  |")
    print("" + board[7] + " | " + board[8] + "| " + board[9])
    print("  |  |")


def check_win(board, mark):
    return (
        (board[1] == board[2] == board[3] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[7] == board[8] == board[9] == mark)
        or (board[1] == board[4] == board[7] == mark)
        or (board[2] == board[5] == board[8] == mark)
        or (board[3] == board[6] == board[9] == mark)
        or (board[1] == board[5] == board[9] == mark)
        or (board[3] == board[5] == board[7] == mark)
    )


def is_board_full(board):
    return " " not in board[1:]


def main():
    board = [" "] * 10
    current_player = "X"

    print("Гра 'Хрестики-нулики'")

    while True:
        display_board(board)
        position = int(
            input("Гравець " + current_player + ", виберіть позицію (1-9): ")
        )

        if board[position] == " ":
            board[position] = current_player

            if check_win(board, current_player):
                display_board(board)
                print("Гравець " + current_player + " переміг!")
                break
            elif is_board_full(board):
                display_board(board)
                print("Нічия!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Ця позиція вже зайнята. Виберіть іншу.")


if __name__ == "__main__":
    main()
