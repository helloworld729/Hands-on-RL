# 五子棋游戏 - 控制台版本
defaultPad = '--'
board = [[defaultPad for _ in range(15)] for _ in range(15)]
def getStrNum(x):
    return '0' + str(x) if x < 10 else str(x)
# 增加y前导
for i in range(15):
    j = getStrNum(i+1)
    board[i] = [j] + board[i]
# 增加x前导
xprefix = [['00'] + [getStrNum(x) for x in list(range(1, 16))]]
board  = xprefix + board

def print_board(board):
    for row in board:
        print(' ' .join(row))
    print()


def check_win(board, player):
    # 检查水平、垂直、对角线是否有五个连续的棋子
    for i in range(1, 15):
        for j in range(11):
            if all(board[i][j + k] == player for k in range(5)):
                return True
            if all(board[i + k][j] == player for k in range(5)):
                return True
            if all(board[i + k][j + k] == player for k in range(5)):
                return True
            if all(board[i + k][j - k] == player for k in range(5)):
                return True
    return False


def is_valid_move(board, row, col):
    # 检查位置是否有效（在棋盘内且该位置为空）
    return 1 <= row <= 15 and 1 <= col <= 15 and board[row][col] == defaultPad


def get_move(player):
    while True:
        try:
            row, col = map(int, input(f"玩家 {player} 的回合，请输入您的落子位置（行 列）：").split())
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("无效的移动，请输入棋盘内未被占用的位置。")
        except (ValueError, IndexError):
            print("输入格式错误，请输入两个数字，用空格分隔。")


def main():
    current_player = 'X'
    while True:
        print_board(board)

        # 可以把这里的get_move改成DQN
        row, col = get_move(current_player)
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"玩家 {current_player} 赢了！")
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()